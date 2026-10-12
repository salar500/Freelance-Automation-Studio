"""Bounded synthetic workload measurements. No generated data belongs in Git."""

import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import platform
try:
    import resource
except ImportError:
    resource = None  # Fixture generation remains usable by Windows tests.
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time

from .core import Engine, JobError, checksum


def synthetic_row(key, field_chars=0):
    return [str(key), f"record-{key}", "x" * field_chars if field_chars else "Δ🌱" + "x" * ((key % 9) * 8)]


def generate(path, rows, unique, *, invalid_at=None, field_chars=0, empty=False):
    with Path(path).open("w", encoding="utf-8", newline="") as stream:
        if empty:
            return
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["id", "label", "notes"])
        for index in range(rows):
            writer.writerow(["invalid"] if index == invalid_at else synthetic_row(index % unique, field_chars))


def disk_sample(workspace):
    """Sample actual allocated blocks, counting hard-linked bytes only once."""
    allocated = partial = database = 0
    seen = set()
    for path in Path(workspace).rglob("*"):
        try:
            if not path.is_file():
                continue
            info = path.stat()
            identity = (info.st_dev, info.st_ino)
            if identity not in seen:
                allocated += info.st_blocks * 512
                seen.add(identity)
            if path.name.endswith(".partial.csv"):
                partial += info.st_size
            if path.name.startswith("jobs.sqlite3"):
                database += info.st_size
        except FileNotFoundError:
            pass  # A journal/publication file disappeared between samples.
    return {"workspace_allocated_bytes": allocated, "partial_bytes": partial, "sqlite_bytes": database}


def child_case(spec):
    if resource is None:
        raise JobError("MEASUREMENT_PLATFORM", "This resource harness requires Linux.")
    # Separate fresh processes make ru_maxrss peaks comparable, including startup.
    resource.setrlimit(resource.RLIMIT_AS, (256 * 1024**2, 256 * 1024**2))
    resource.setrlimit(resource.RLIMIT_CPU, (60, 65))
    source, workspace = Path(spec["source"]), Path(spec["workspace"])
    original = checksum(source)
    engine = Engine(workspace, max_rows=spec.get("max_rows", 100_000))
    database_before = engine.db_path.stat().st_size
    create_seconds = processing_seconds = cpu_seconds = 0.0
    cancellation_seconds = None
    results = []
    for _ in range(spec.get("repeats", 1)):
        start = time.perf_counter()
        job = engine.create(source)
        create_seconds += time.perf_counter() - start
        cancel_at = None
        def progress(event):
            nonlocal cancel_at
            if spec.get("cancel_at") and event["input_rows"] >= spec["cancel_at"] and cancel_at is None:
                cancel_at = time.perf_counter()
                engine.cancel(job["id"])
        start, cpu_start = time.perf_counter(), time.process_time()
        code = None
        try:
            result = engine.run(job["id"], progress if spec.get("cancel_at") else None)
        except JobError as exc:
            code = exc.code
            result = engine.inspect(job["id"])
        processing_seconds += time.perf_counter() - start
        cpu_seconds += time.process_time() - cpu_start
        if cancel_at is not None:
            cancellation_seconds = time.perf_counter() - cancel_at
        assert result["state"] == spec.get("expected_state", "REVIEW_REQUIRED"), (spec["name"], result["state"], code)
        if spec.get("expected_error"):
            assert code == spec["expected_error"], (code, spec["expected_error"])
        assert not result["delivery_approved"]
        if result["state"] == "REVIEW_REQUIRED":
            artifact = result["artifacts"][-1]
            output = workspace / artifact["path"]
            assert checksum(output) == artifact["sha256"]
            # Analytic first-occurrence oracle, not a second implementation of dedup.
            with output.open(encoding="utf-8", newline="") as stream:
                reader = csv.reader(stream)
                assert next(reader) == ["id", "label", "notes"]
                for key in range(spec["unique"]):
                    assert next(reader) == synthetic_row(key, spec.get("field_chars", 0))
                assert next(reader, None) is None
        results.append({"job_id": result["id"], "state": result["state"], "error": code,
                        "rows_processed": result["attempts"][-1]["input_rows"],
                        "unique_rows": result["attempts"][-1]["output_rows"],
                        "output_bytes": sum(a["bytes"] for a in result["artifacts"] if a["status"] == "VERIFIED"),
                        "sha256": [a["sha256"] for a in result["artifacts"] if a["status"] == "VERIFIED"]})
    assert checksum(source) == original
    if len(results) > 1:
        assert results[0]["sha256"] == results[-1]["sha256"]
    start = time.perf_counter()
    recovery = engine.recover()
    recovery_seconds = time.perf_counter() - start
    stable = engine.inspect(results[-1]["job_id"])
    second_recovery = engine.recover()
    assert engine.inspect(results[-1]["job_id"]) == stable
    assert second_recovery["interrupted_attempts"] == second_recovery["invalidated_artifacts"] == 0
    with sqlite3.connect(engine.db_path) as database:
        assert database.execute("PRAGMA integrity_check").fetchone()[0] == "ok"
        assert database.execute("PRAGMA foreign_key_check").fetchall() == []
        assert database.execute("SELECT COUNT(*) FROM jobs").fetchone()[0] == len(results)
        assert database.execute("SELECT COUNT(*) FROM attempts").fetchone()[0] == len(results)
    usage = resource.getrusage(resource.RUSAGE_SELF)
    return {"name": spec["name"], "status": "PASS", "rows": spec["rows"], "repeats": spec.get("repeats", 1),
            "create_seconds": create_seconds, "execution_seconds": processing_seconds, "cpu_seconds": cpu_seconds,
            "cpu_percent_one_core": 100 * cpu_seconds / processing_seconds if processing_seconds else 0,
            "peak_rss_mib": usage.ru_maxrss / 1024, "input_bytes": source.stat().st_size,
            "sqlite_growth_bytes": engine.db_path.stat().st_size - database_before,
            "throughput_rows_s": sum(x["rows_processed"] for x in results) / processing_seconds,
            "cancellation_seconds": cancellation_seconds, "recovery_seconds": recovery_seconds,
            "results": results, "recovery": recovery, "input_unchanged": True, "repeat_recovery_idempotent": True,
            "sqlite_integrity": "ok", "sqlite_history_correct": True}


def run_case(root, spec):
    case_dir = Path(root) / spec["name"]
    case_dir.mkdir()
    source, workspace = case_dir / "synthetic.csv", case_dir / "workspace"
    generate(source, spec["rows"], spec["unique"], invalid_at=spec.get("invalid_at"),
             field_chars=spec.get("field_chars", 0), empty=spec.get("empty", False))
    if source.stat().st_size > 32 * 1024**2:
        return {"name": spec["name"], "status": "SKIPPED", "reason": "Generated input exceeds default 32 MiB bound."}
    spec = dict(spec, source=str(source), workspace=str(workspace))
    spec_path = case_dir / "case.json"
    spec_path.write_text(json.dumps(spec))
    child = subprocess.Popen([sys.executable, "-m", "experiments.p5_portable_core.workloads", "--child", str(spec_path)],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    peak = {"workspace_allocated_bytes": 0, "partial_bytes": 0, "sqlite_bytes": 0}
    start = time.perf_counter()
    try:
        while child.poll() is None:
            sample = disk_sample(workspace)
            peak = {key: max(peak[key], sample[key]) for key in peak}
            if time.perf_counter() - start > 120:
                child.kill()
                out, err = child.communicate()
                return {"name": spec["name"], "status": "FAIL", "reason": "120-second parent watchdog terminated owned child."}
            time.sleep(0.01)
        out, err = child.communicate()
    finally:
        if child.poll() is None:
            child.kill()
            child.communicate()
    if child.returncode:
        return {"name": spec["name"], "status": "FAIL", "exit_code": child.returncode, "diagnostic": err[-1500:]}
    sample = disk_sample(workspace)
    peak = {key: max(peak[key], sample[key]) for key in peak}
    return dict(json.loads(out), sampled_disk_peak=peak, sample_interval_seconds=0.01,
                final_disk=sample, evidence_directory=str(case_dir))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--child", help=argparse.SUPPRESS)
    parser.add_argument("--output")
    parser.add_argument("--baseline", action="store_true", help="Measure 1k/10k before optimization")
    parser.add_argument("--include-500k", action="store_true")
    args = parser.parse_args()
    if args.child:
        print(json.dumps(child_case(json.loads(Path(args.child).read_text()))))
        return 0
    if not args.output:
        parser.error("--output is required")
    root = Path(tempfile.mkdtemp(prefix="fas-p5-workloads-", dir="/tmp"))
    cases = [{"name": "1k_duplicate", "rows": 1000, "unique": 100},
             {"name": "10k_unique", "rows": 10000, "unique": 9500}]
    if not args.baseline:
        cases = [{"name": "empty", "rows": 0, "unique": 0, "empty": True, "expected_state": "FAILED", "expected_error": "INPUT_HEADERS"},
                 {"name": "header_only", "rows": 0, "unique": 0}, {"name": "small", "rows": 10, "unique": 3},
                 *cases, {"name": "1k_unique", "rows": 1000, "unique": 950},
                 {"name": "10k_duplicate", "rows": 10000, "unique": 1000},
                 {"name": "100k_duplicate", "rows": 100000, "unique": 1000},
                 {"name": "100k_unique", "rows": 100000, "unique": 95000},
                 {"name": "default_row_limit", "rows": 100001, "unique": 1000, "expected_state": "FAILED", "expected_error": "ROW_LIMIT"},
                 {"name": "invalid", "rows": 1000, "unique": 900, "invalid_at": 500, "expected_state": "FAILED", "expected_error": "INPUT_SCHEMA"},
                 {"name": "large_fields", "rows": 10, "unique": 10, "field_chars": 100000},
                 {"name": "oversized_field", "rows": 1, "unique": 1, "field_chars": 200000, "expected_state": "FAILED", "expected_error": "FIELD_LIMIT"},
                 {"name": "cancel_100k", "rows": 100000, "unique": 95000, "cancel_at": 1000, "expected_state": "CANCELLED"},
                 {"name": "repeat_10k", "rows": 10000, "unique": 9500, "repeats": 2}]
    report = {"environment": {"platform": platform.system(), "python": platform.python_version(), "sqlite": sqlite3.sqlite_version,
                              "cpu_visible": os.cpu_count(), "tmp_free_bytes": shutil.disk_usage(root).free},
              "method": "Fresh serial Linux children;256MiB RLIMIT_AS,60sCPU/120swatchdog;ru_maxrss KiB;process_time CPU;10ms disk samples lower-bound peaks.",
              "evidence_root": str(root), "cases": []}
    for spec in cases:
        row = run_case(root, spec)
        report["cases"].append(row)
        print(json.dumps({key: row.get(key) for key in ["name", "status", "execution_seconds", "peak_rss_mib", "throughput_rows_s"]}), flush=True)
        Path(args.output).write_text(json.dumps(report, indent=2))
        if row["status"] == "FAIL":
            return 1
    if args.include_500k and not args.baseline:
        measured = next(x for x in report["cases"] if x["name"] == "100k_duplicate")
        profiles = [{"name": "500k_duplicate", "rows": 500000, "unique": 1000, "max_rows": 500000},
                    {"name": "500k_unique_budget", "rows": 500000, "unique": 475000, "max_rows": 500000,
                     "expected_state": "FAILED", "expected_error": "RESOURCE_MEMORY"}]
        for spec in profiles:
            if measured["peak_rss_mib"] < 128 and measured["execution_seconds"] < 15 and shutil.disk_usage(root).free > 256 * 1024**2:
                row = run_case(root, spec)
            else:
                row = {"name": spec["name"], "status": "SKIPPED", "reason": "100k measurements or disk headroom failed admission checks."}
            report["cases"].append(row)
            print(json.dumps({key: row.get(key) for key in ["name", "status", "execution_seconds", "peak_rss_mib"]}), flush=True)
            Path(args.output).write_text(json.dumps(report, indent=2))
    return 1 if any(x["status"] == "FAIL" for x in report["cases"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
