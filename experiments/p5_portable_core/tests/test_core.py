import csv
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from experiments.p5_portable_core.core import Engine, JobError, checksum


class CoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="fas-p5-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.engine = Engine(self.root / "workspace")

    def input(self, text="id,name\n1,Ada\n2,Lin\n1,Ada\n"):
        source = self.root / "synthetic.csv"
        source.write_text(text, encoding="utf-8", newline="")
        return source

    def execute(self, text):
        job = self.engine.create(self.input(text))
        return self.engine.run(job["id"])

    def test_exact_dedup_preserves_first_order_and_original(self):
        source = self.input()
        original = source.read_bytes()
        events = []
        job = self.engine.create(source)
        result = self.engine.run(job["id"], events.append)
        artifact = result["artifacts"][0]
        output = self.engine.root / artifact["path"]
        with output.open(newline="") as stream:
            self.assertEqual(list(csv.reader(stream)), [["id", "name"], ["1", "Ada"], ["2", "Lin"]])
        self.assertEqual(source.read_bytes(), original)
        self.assertEqual(artifact["sha256"], checksum(output))
        self.assertEqual(result["state"], "REVIEW_REQUIRED")
        self.assertFalse(result["delivery_approved"])
        self.assertEqual(result["attempts"][0]["input_rows"], 3)
        self.assertEqual(result["attempts"][0]["output_rows"], 2)
        self.assertEqual([e["input_rows"] for e in events], [1, 2, 3])

    def test_persistence_reopen(self):
        job = self.engine.create(self.input())
        reopened = Engine(self.engine.root)
        self.assertEqual(reopened.inspect(job["id"])["state"], "READY")
        self.assertEqual(reopened.run(job["id"])["state"], "REVIEW_REQUIRED")

    def test_missing_input(self):
        with self.assertRaises(JobError) as caught:
            self.engine.create(self.root / "absent.csv")
        self.assertEqual(caught.exception.code, "INPUT_MISSING")

    def test_size_limit(self):
        engine = Engine(self.engine.root, max_input_bytes=2)
        with self.assertRaises(JobError) as caught:
            engine.create(self.input())
        self.assertEqual(caught.exception.code, "INPUT_TOO_LARGE")

    def test_headers_invalid(self):
        for text in ("", "id,id\n1,1\n", "id,\n1,2\n"):
            with self.subTest(text=text), self.assertRaises(JobError) as caught:
                self.execute(text)
            self.assertEqual(caught.exception.code, "INPUT_HEADERS")

    def test_row_width_failure_is_persisted_without_eligible_output(self):
        job = self.engine.create(self.input("id,name\n1\n"))
        with self.assertRaises(JobError) as caught:
            self.engine.run(job["id"])
        self.assertEqual(caught.exception.code, "INPUT_SCHEMA")
        failed = self.engine.inspect(job["id"])
        self.assertEqual(failed["state"], "FAILED")
        self.assertEqual(failed["error"]["code"], "INPUT_SCHEMA")
        self.assertEqual(failed["artifacts"], [])

    def test_invalid_utf8(self):
        source = self.input()
        source.write_bytes(b"id,name\n1,\xff\n")
        job = self.engine.create(source)
        with self.assertRaises(JobError) as caught:
            self.engine.run(job["id"])
        self.assertEqual(caught.exception.code, "INPUT_ENCODING")

    def test_malformed_quoted_csv(self):
        with self.assertRaises(JobError) as caught:
            self.execute('id,name\n1,"unfinished\n')
        self.assertEqual(caught.exception.code, "INPUT_CSV")

    def test_header_only_output(self):
        result = self.execute("id,name\n")
        self.assertEqual(result["attempts"][0]["output_rows"], 0)
        self.assertEqual(result["artifacts"][0]["status"], "VERIFIED")

    def test_quoted_unicode_and_multiline_cells(self):
        result = self.execute('id,name\n1,"Zoë, A\nB"\n1,"Zoë, A\nB"\n')
        output = self.engine.root / result["artifacts"][0]["path"]
        with output.open(newline="", encoding="utf-8") as stream:
            self.assertEqual(list(csv.reader(stream)), [["id", "name"], ["1", "Zoë, A\nB"]])

    def test_values_are_exact_not_fuzzy_or_formula_evaluated(self):
        result = self.execute('id,value\n1, Ada\n1,Ada\n2,=1+1\n2,=1+1\n')
        self.assertEqual(result["attempts"][0]["output_rows"], 3)

    def test_row_boundary(self):
        self.engine.max_rows = 2
        result = self.execute("id\n1\n2\n")
        self.assertEqual(result["attempts"][0]["input_rows"], 2)
        with self.assertRaises(JobError) as caught:
            self.execute("id\n1\n2\n3\n")
        self.assertEqual(caught.exception.code, "ROW_LIMIT")

    def test_snapshot_detects_tampering(self):
        job = self.engine.create(self.input())
        (self.engine.root / job["input_path"]).write_text("changed")
        with self.assertRaises(JobError) as caught:
            self.engine.run(job["id"])
        self.assertEqual(caught.exception.code, "INPUT_INTEGRITY")

    def test_input_snapshot_is_independent_of_source_later_changes(self):
        source = self.input()
        job = self.engine.create(source)
        source.write_text("id,name\n9,Changed\n")
        result = self.engine.run(job["id"])
        self.assertEqual(result["attempts"][0]["output_rows"], 2)

    def test_cooperative_cancel_and_explicit_retry_keep_history(self):
        job = self.engine.create(self.input())
        def progress(event):
            if event["phase"] == "RUNNING":
                self.engine.cancel(job["id"])
        result = self.engine.run(job["id"], progress)
        self.assertEqual(result["state"], "CANCELLED")
        self.assertEqual(result["attempts"][0]["input_rows"], 1)
        self.assertEqual(result["artifacts"], [])
        retry = self.engine.run(job["id"])
        self.assertEqual([a["outcome"] for a in retry["attempts"]], ["CANCELLED", "SUCCEEDED"])

    def test_cancel_before_start(self):
        job = self.engine.create(self.input())
        self.engine.cancel(job["id"])
        result = self.engine.run(job["id"])
        self.assertEqual(result["state"], "CANCELLED")
        self.assertEqual(result["attempts"][0]["input_rows"], 0)

    def test_completed_job_cannot_restart_or_cancel(self):
        job = self.execute("id\n1\n")
        for operation in (self.engine.run, self.engine.cancel):
            with self.assertRaises(JobError) as caught:
                operation(job["id"])
            self.assertEqual(caught.exception.code, "INVALID_STATE")

    def test_no_success_inferred_after_actual_process_exit(self):
        job = self.engine.create(self.input())
        script = ("import os,sys; from experiments.p5_portable_core.core import Engine; "
                  "Engine(sys.argv[1]).run(sys.argv[2], lambda event: os._exit(17))")
        process = subprocess.run([sys.executable, "-c", script, str(self.engine.root), job["id"]],
                                 capture_output=True, text=True)
        self.assertEqual(process.returncode, 17)
        recovered = Engine(self.engine.root)
        self.assertEqual(recovered.recover()["interrupted_attempts"], 1)
        self.assertEqual(recovered.inspect(job["id"])["state"], "INTERRUPTED")
        self.assertEqual(recovered.recover()["interrupted_attempts"], 0)
        self.assertEqual(recovered.run(job["id"])["state"], "REVIEW_REQUIRED")

    def test_prepared_publication_interruption_is_quarantined(self):
        class Crash(BaseException):
            pass
        job = self.engine.create(self.input())
        with patch("experiments.p5_portable_core.core.os.link", side_effect=Crash), self.assertRaises(Crash):
            self.engine.run(job["id"])
        self.engine.recover()
        result = self.engine.inspect(job["id"])
        self.assertEqual(result["state"], "INTERRUPTED")
        self.assertEqual(result["artifacts"][0]["status"], "QUARANTINED")

    def test_recovery_refuses_active_coordinator(self):
        with self.engine._execution_lock(), self.assertRaises(JobError) as caught:
            Engine(self.engine.root).recover()
        self.assertEqual(caught.exception.code, "BUSY")

    def test_output_tamper_invalidates_eligibility(self):
        result = self.execute("id\n1\n")
        self.assertEqual(self.engine.verify(result["id"])["artifacts_verified"], 1)
        output = self.engine.root / result["artifacts"][0]["path"]
        output.write_text("id\nBAD\n")
        with self.assertRaises(JobError) as caught:
            self.engine.verify(result["id"])
        self.assertEqual(caught.exception.code, "OUTPUT_INTEGRITY")
        self.assertEqual(self.engine.inspect(result["id"])["state"], "REVISION_REQUIRED")

    def test_storage_failure_preserves_original_and_structured_failure(self):
        source = self.input()
        original = source.read_bytes()
        job = self.engine.create(source)
        with patch("experiments.p5_portable_core.core.os.link", side_effect=OSError), self.assertRaises(JobError) as caught:
            self.engine.run(job["id"])
        self.assertEqual(caught.exception.code, "STORAGE_ERROR")
        self.assertEqual(source.read_bytes(), original)
        self.assertEqual(self.engine.inspect(job["id"])["artifacts"][0]["status"], "QUARANTINED")

    def test_publication_never_overwrites_existing_destination(self):
        job = self.engine.create(self.input())
        original_link = os.link
        destinations = []
        def collision(source, destination):
            Path(destination).write_text("EXISTING_BYTES")
            destinations.append(Path(destination))
            original_link(source, destination)
        with patch("experiments.p5_portable_core.core.os.link", side_effect=collision), self.assertRaises(JobError):
            self.engine.run(job["id"])
        self.assertEqual(destinations[0].read_text(), "EXISTING_BYTES")
        self.assertEqual(self.engine.inspect(job["id"])["state"], "FAILED")

    def test_unexpected_processing_error_is_safe(self):
        job = self.engine.create(self.input())
        def fail(event):
            raise ValueError("SECRET_SHOULD_NOT_LEAK")
        with self.assertRaises(JobError) as caught:
            self.engine.run(job["id"], fail)
        self.assertEqual(caught.exception.code, "INTERNAL_ERROR")
        self.assertNotIn("SECRET", json.dumps(self.engine.inspect(job["id"])))

    def test_missing_job_and_no_output_errors(self):
        with self.assertRaises(JobError) as caught:
            self.engine.inspect("not-a-job")
        self.assertEqual(caught.exception.code, "JOB_NOT_FOUND")
        job = self.engine.create(self.input())
        with self.assertRaises(JobError) as caught:
            self.engine.verify(job["id"])
        self.assertEqual(caught.exception.code, "NO_VERIFIED_OUTPUT")

    def test_deterministic_output_across_attempts_and_sqlite_integrity(self):
        first = self.execute("id,name\n1,Ada\n1,Ada\n2,Lin\n")
        second = self.execute("id,name\n1,Ada\n1,Ada\n2,Lin\n")
        self.assertEqual(first["artifacts"][0]["sha256"], second["artifacts"][0]["sha256"])
        with sqlite3.connect(self.engine.db_path) as db:
            self.assertEqual(db.execute("PRAGMA integrity_check").fetchone()[0], "ok")
            self.assertEqual(db.execute("PRAGMA foreign_key_check").fetchall(), [])
            self.assertGreater(db.execute("SELECT COUNT(*) FROM events").fetchone()[0], 0)


class CLIIntegrationTests(unittest.TestCase):
    def test_cancellation_from_separate_connection_while_worker_is_active(self):
        with tempfile.TemporaryDirectory(prefix="fas-p5-cross-process-") as folder:
            root = Path(folder)
            source = root / "synthetic.csv"
            source.write_text("id\n1\n2\n3\n")
            engine = Engine(root / "data")
            job = engine.create(source)
            script = ("import sys,json; from experiments.p5_portable_core.core import Engine; "
                      "e=Engine(sys.argv[1]); "
                      "result=e.run(sys.argv[2], lambda event: "
                      "(print('PROGRESS',flush=True),sys.stdin.readline()) "
                      "if event['phase']=='RUNNING' else None); print(json.dumps(result))")
            process = subprocess.Popen([sys.executable, "-c", script, str(engine.root), job["id"]],
                                       stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       text=True)
            try:
                self.assertEqual(process.stdout.readline().strip(), "PROGRESS")
                engine.cancel(job["id"])
                out, err = process.communicate("continue\n", timeout=5)
                self.assertEqual(process.returncode, 0, err)
                result = json.loads(out)
                self.assertEqual(result["state"], "CANCELLED")
                self.assertEqual(result["attempts"][0]["input_rows"], 1)
            finally:
                if process.poll() is None:
                    process.kill()
                    process.communicate()

    def test_cli_single_command_process(self):
        with tempfile.TemporaryDirectory(prefix="fas-p5-process-") as folder:
            process = subprocess.run([sys.executable, "-m", "experiments.p5_portable_core",
                                      "--workspace", folder, "process",
                                      "experiments/p5_portable_core/fixtures/duplicates.csv"],
                                     capture_output=True, text=True)
            self.assertEqual(process.returncode, 0, process.stderr)
            result = json.loads(process.stdout)
            self.assertEqual(result["attempts"][0]["input_rows"], 5)
            self.assertEqual(result["attempts"][0]["output_rows"], 3)

    def test_real_cli_create_run_verify_and_cancellation(self):
        with tempfile.TemporaryDirectory(prefix="fas-p5-cli-") as folder:
            root = Path(folder)
            source = root / "synthetic.csv"
            source.write_text("id,name\n1,Ada\n1,Ada\n2,Lin\n")
            command = [sys.executable, "-m", "experiments.p5_portable_core", "--workspace", str(root / "data")]
            def invoke(*args):
                return subprocess.run(command + list(args), capture_output=True, text=True)
            created = invoke("create", str(source))
            self.assertEqual(created.returncode, 0, created.stderr)
            job_id = json.loads(created.stdout)["id"]
            run = invoke("run", job_id)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertIn('"progress"', run.stderr)
            self.assertEqual(json.loads(run.stdout)["state"], "REVIEW_REQUIRED")
            self.assertEqual(invoke("verify", job_id).returncode, 0)
            another = json.loads(invoke("create", str(source)).stdout)["id"]
            cancelled = invoke("run", another, "--cancel-after-rows", "1")
            self.assertEqual(cancelled.returncode, 2)
            self.assertEqual(json.loads(cancelled.stdout)["state"], "CANCELLED")
            error = invoke("run", "missing")
            self.assertEqual(error.returncode, 1)
            self.assertEqual(json.loads(error.stderr)["error"]["code"], "JOB_NOT_FOUND")


if __name__ == "__main__":
    unittest.main()
