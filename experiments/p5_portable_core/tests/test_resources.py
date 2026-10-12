"""Deterministic regression checks for portable-core resource protections."""

from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from experiments.p5_portable_core.core import Engine, JobError
from experiments.p5_portable_core.workloads import generate


class ResourceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="fas-p5-resource-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "synthetic.csv"
        generate(self.source, 10, 8)

    def engine(self, **options):
        return Engine(self.root / "workspace", **options)

    def assert_run_error(self, engine, code):
        original = self.source.read_bytes()
        job = engine.create(self.source)
        with self.assertRaises(JobError) as caught:
            engine.run(job["id"])
        self.assertEqual(caught.exception.code, code)
        result = engine.inspect(job["id"])
        self.assertEqual(result["state"], "FAILED")
        self.assertFalse(result["delivery_approved"])
        self.assertEqual(self.source.read_bytes(), original)
        return result

    def test_field_limit_applies_to_values_and_headers(self):
        for text in ("id,name\n1,abcdef\n", "longheader,name\n1,A\n"):
            with self.subTest(text=text):
                self.source.write_text(text)
                self.assert_run_error(self.engine(max_field_chars=4), "FIELD_LIMIT")

    def test_parser_field_limit_has_stable_resource_error(self):
        generate(self.source, 1, 1, field_chars=200000)
        self.assert_run_error(self.engine(), "FIELD_LIMIT")

    def test_column_limit(self):
        self.assert_run_error(self.engine(max_columns=2), "COLUMN_LIMIT")

    def test_unique_memory_budget_rejects_safely(self):
        self.assert_run_error(self.engine(max_unique_memory_bytes=512), "RESOURCE_MEMORY")

    def test_disk_reserve_rejects_snapshot_without_modifying_source(self):
        engine = self.engine()
        original = self.source.read_bytes()
        with patch("experiments.p5_portable_core.core.shutil.disk_usage", return_value=shutil._ntuple_diskusage(1024,1024,0)), self.assertRaises(JobError) as caught:
            engine.create(self.source)
        self.assertEqual(caught.exception.code, "RESOURCE_DISK")
        self.assertEqual(self.source.read_bytes(), original)

    def test_disk_preflight_failure_records_failed_attempt(self):
        engine = self.engine()
        job = engine.create(self.source)
        with patch("experiments.p5_portable_core.core.shutil.disk_usage", return_value=shutil._ntuple_diskusage(1024,1024,0)), self.assertRaises(JobError) as caught:
            engine.run(job["id"])
        self.assertEqual(caught.exception.code, "RESOURCE_DISK")
        self.assertEqual(engine.inspect(job["id"])["state"], "FAILED")

    def test_disk_space_loss_during_processing_is_detected(self):
        engine = self.engine(checkpoint_rows=2)
        job = engine.create(self.source)
        usage = [shutil._ntuple_diskusage(10**9,0,10**9), shutil._ntuple_diskusage(1024,1024,0)]
        with patch("experiments.p5_portable_core.core.shutil.disk_usage", side_effect=usage), self.assertRaises(JobError) as caught:
            engine.run(job["id"])
        self.assertEqual(caught.exception.code, "RESOURCE_DISK")
        result = engine.inspect(job["id"])
        self.assertEqual(result["attempts"][-1]["input_rows"], 2)
        self.assertEqual(result["state"], "FAILED")

    def test_deadline_is_cooperative_and_structured(self):
        engine = self.engine(timeout_seconds=30)
        job = engine.create(self.source)
        with patch("experiments.p5_portable_core.core.time.monotonic", side_effect=[0,0,31]), self.assertRaises(JobError) as caught:
            engine.run(job["id"])
        self.assertEqual(caught.exception.code, "RESOURCE_TIMEOUT")
        self.assertEqual(engine.inspect(job["id"])["state"], "FAILED")

    def test_expired_finalization_deadline_quarantines_published_file(self):
        clock = [0]
        def hook(name, context):
            if name == "before_terminal_commit":
                clock[0] = 100
        engine = self.engine(timeout_seconds=30, fault_hook=hook)
        job = engine.create(self.source)
        with patch("experiments.p5_portable_core.core.time.monotonic", side_effect=lambda:clock[0]), self.assertRaises(JobError) as caught:
            engine.run(job["id"])
        self.assertEqual(caught.exception.code, "RESOURCE_TIMEOUT")
        result = engine.inspect(job["id"])
        self.assertEqual(result["artifacts"][-1]["status"], "QUARANTINED")
        self.assertFalse(result["delivery_approved"])

    def test_progress_writes_are_batched_but_terminal_counts_are_exact(self):
        generate(self.source, 1000, 950)
        engine = self.engine(checkpoint_rows=100)
        job = engine.create(self.source)
        with patch.object(engine, "_persist_progress", wraps=engine._persist_progress) as calls:
            result = engine.run(job["id"])
        self.assertLessEqual(calls.call_count, 11)
        self.assertEqual(result["attempts"][-1]["input_rows"], 1000)
        self.assertEqual(result["attempts"][-1]["output_rows"], 950)

    def test_cancellation_flushes_counts_before_checkpoint_boundary(self):
        engine = self.engine(checkpoint_rows=1000)
        job = engine.create(self.source)
        def progress(event):
            if event["input_rows"] == 7:
                engine.cancel(job["id"])
        result = engine.run(job["id"], progress)
        self.assertEqual(result["state"], "CANCELLED")
        self.assertEqual(result["attempts"][-1]["input_rows"], 7)
        engine.recover()
        before = engine.inspect(job["id"])
        engine.recover()
        self.assertEqual(engine.inspect(job["id"]), before)

    def test_invalid_resource_configuration(self):
        for options in ({"checkpoint_rows":0},{"max_rows":0},{"timeout_seconds":float('inf')},
                        {"min_free_bytes":-1},{"max_unique_memory_bytes":0}):
            with self.subTest(options=options), self.assertRaises(JobError) as caught:
                self.engine(**options)
            self.assertEqual(caught.exception.code, "RESOURCE_CONFIG")

    def test_cli_progress_volume_is_bounded(self):
        generate(self.source, 1000, 950)
        result = subprocess.run([sys.executable,"-m","experiments.p5_portable_core",
                                 "--workspace",str(self.root/'workspace'),"process",str(self.source)],
                                capture_output=True,text=True,timeout=10)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertLessEqual(len(result.stderr.splitlines()),11)
        self.assertEqual(json.loads(result.stdout)['attempts'][-1]['input_rows'],1000)

    def test_batched_progress_crash_preserves_last_durable_count_not_false_success(self):
        generate(self.source,1000,950)
        engine = self.engine(checkpoint_rows=100)
        job = engine.create(self.source)
        original = self.source.read_bytes()
        script = ("import os,sys; from experiments.p5_portable_core.core import Engine; "
                  "Engine(sys.argv[1],checkpoint_rows=100).run(sys.argv[2], "
                  "lambda event: os._exit(27) if event['input_rows']==205 else None)")
        result = subprocess.run([sys.executable,'-c',script,str(engine.root),job['id']],
                                capture_output=True,text=True,timeout=10)
        self.assertEqual(result.returncode,27,result.stderr)
        self.assertEqual(engine.inspect(job['id'])['attempts'][-1]['input_rows'],200)
        self.assertEqual(engine.recover()['interrupted_attempts'],1)
        recovered = engine.inspect(job['id'])
        self.assertEqual(recovered['state'],'INTERRUPTED')
        self.assertFalse(recovered['delivery_approved'])
        self.assertEqual(self.source.read_bytes(),original)


if __name__ == "__main__":
    unittest.main()
