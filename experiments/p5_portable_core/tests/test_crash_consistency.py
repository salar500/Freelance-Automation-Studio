"""Deterministic failpoints and real process death, using only synthetic data."""

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


class CrashConsistencyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="fas-p5-crash-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "synthetic.csv"
        self.source.write_text("id,name\n1,Ada\n2,Lin\n1,Ada\n")
        self.original = self.source.read_bytes()
        self.engine = Engine(self.root / "data")
        self.job = self.engine.create(self.source)

    def abrupt_exit_at(self, point):
        script = ("import os,sys; from experiments.p5_portable_core.core import Engine; "
                  "hook=lambda point,context: os._exit(23) if point==sys.argv[3] else None; "
                  "Engine(sys.argv[1],fault_hook=hook).run(sys.argv[2])")
        child = subprocess.run([sys.executable, "-c", script, str(self.engine.root), self.job["id"], point],
                               capture_output=True, text=True, timeout=10)
        self.assertEqual(child.returncode, 23, child.stderr)
        self.assertEqual(self.source.read_bytes(), self.original)
        return self.engine.recover()

    def assert_repeat_is_idempotent(self):
        before = self.engine.inspect(self.job["id"])
        with sqlite3.connect(self.engine.db_path) as db:
            events = db.execute("SELECT COUNT(*) FROM events").fetchone()[0]
        again = self.engine.recover()
        self.assertEqual(again["interrupted_attempts"], 0)
        self.assertEqual(again["invalidated_artifacts"], 0)
        self.assertEqual(self.engine.inspect(self.job["id"]), before)
        with sqlite3.connect(self.engine.db_path) as db:
            self.assertEqual(db.execute("SELECT COUNT(*) FROM events").fetchone()[0], events)
            self.assertEqual(db.execute("PRAGMA integrity_check").fetchone()[0], "ok")

    def test_crash_before_artifact_write(self):
        result = self.abrupt_exit_at("attempt_started")
        self.assertEqual(result["interrupted_attempts"], 1)
        job = self.engine.inspect(self.job["id"])
        self.assertEqual(job["state"], "INTERRUPTED")
        self.assertEqual(job["attempts"][0]["recovery"]["staging"]["state"], "MISSING")
        self.assertEqual(job["artifacts"], [])
        self.assert_repeat_is_idempotent()

    def test_crash_during_temporary_write(self):
        result = self.abrupt_exit_at("row_written")
        self.assertEqual(result["issues"][0]["code"], "RECOVERY_PARTIAL_OUTPUT")
        job = self.engine.inspect(self.job["id"])
        artifact = job["artifacts"][0]
        self.assertEqual(artifact["status"], "QUARANTINED")
        self.assertTrue(artifact["path"].endswith("output.partial.csv"))
        self.assertEqual((self.engine.root / artifact["path"]).read_text(), "id,name\n1,Ada\n")
        self.assertEqual(checksum(self.engine.root / artifact["path"]), artifact["sha256"])
        self.assert_repeat_is_idempotent()

    def test_crash_after_staging_creation_before_metadata(self):
        self.abrupt_exit_at("staging_written")
        job = self.engine.inspect(self.job["id"])
        self.assertEqual(job["artifacts"][0]["status"], "QUARANTINED")
        self.assertEqual(job["state"], "INTERRUPTED")
        self.assertFalse(job["delivery_approved"])
        self.assert_repeat_is_idempotent()

    def test_crash_after_prepared_metadata_before_publication(self):
        self.abrupt_exit_at("artifact_prepared")
        artifact = self.engine.inspect(self.job["id"])["artifacts"][0]
        self.assertEqual(artifact["recovery"]["staging"]["state"], "MATCH")
        self.assertEqual(artifact["recovery"]["final"]["state"], "MISSING")
        self.assertEqual(artifact["status"], "QUARANTINED")
        self.assert_repeat_is_idempotent()

    def test_crash_after_publication_before_terminal_db_update(self):
        self.abrupt_exit_at("output_published")
        artifact = self.engine.inspect(self.job["id"])["artifacts"][0]
        self.assertEqual(artifact["recovery"]["final"]["state"], "MATCH")
        self.assertEqual(artifact["recovery"]["staging"]["state"], "MATCH")
        self.assertEqual(artifact["status"], "QUARANTINED")
        self.assertFalse(self.engine.inspect(self.job["id"])["delivery_approved"])
        self.assert_repeat_is_idempotent()

    def test_crash_after_staging_unlink_before_terminal_commit(self):
        self.abrupt_exit_at("before_terminal_commit")
        artifact = self.engine.inspect(self.job["id"])["artifacts"][0]
        self.assertEqual(artifact["recovery"]["final"]["state"], "MATCH")
        self.assertEqual(artifact["recovery"]["staging"]["state"], "MISSING")
        self.assertEqual(artifact["status"], "QUARANTINED")
        self.assert_repeat_is_idempotent()

    def test_crash_after_terminal_metadata_commit_never_approves(self):
        result = self.abrupt_exit_at("terminal_committed")
        self.assertEqual(result["interrupted_attempts"], 0)
        job = self.engine.inspect(self.job["id"])
        self.assertEqual(job["state"], "REVIEW_REQUIRED")
        self.assertEqual(job["attempts"][0]["outcome"], "SUCCEEDED")
        self.assertEqual(job["artifacts"][0]["status"], "VERIFIED")
        self.assertEqual(job["attempts"][0]["review"], "PENDING")
        self.assertFalse(job["delivery_approved"])
        self.assert_repeat_is_idempotent()

    def test_missing_completed_output_is_detected_and_durable(self):
        job = self.engine.run(self.job["id"])
        (self.engine.root / job["artifacts"][0]["path"]).unlink()
        result = self.engine.recover()
        self.assertEqual(result["invalidated_artifacts"], 1)
        self.assertEqual(result["issues"][0]["code"], "RECOVERY_MISSING")
        updated = self.engine.inspect(self.job["id"])
        self.assertEqual(updated["state"], "REVISION_REQUIRED")
        self.assertEqual(updated["attempts"][0]["validation"], "FAILED")
        self.assertEqual(updated["artifacts"][0]["recovery"]["state"], "MISSING")
        self.assert_repeat_is_idempotent()

    def test_tampered_completed_output_is_detected(self):
        job = self.engine.run(self.job["id"])
        (self.engine.root / job["artifacts"][0]["path"]).write_text("id,name\nBAD,VALUE\n")
        result = self.engine.recover()
        self.assertEqual(result["issues"][0]["code"], "RECOVERY_TAMPERED")
        self.assertEqual(self.engine.inspect(self.job["id"])["state"], "REVISION_REQUIRED")
        self.assert_repeat_is_idempotent()

    def test_fsync_disk_failure_never_produces_eligible_output(self):
        with patch("experiments.p5_portable_core.core.os.fsync", side_effect=OSError("disk full")), self.assertRaises(JobError) as caught:
            self.engine.run(self.job["id"])
        self.assertEqual(caught.exception.code, "STORAGE_ERROR")
        job = self.engine.inspect(self.job["id"])
        self.assertEqual(job["state"], "FAILED")
        self.assertEqual(job["artifacts"], [])
        self.assertEqual(self.source.read_bytes(), self.original)

    def test_write_failure_partial_bytes_are_indexed_without_changing_outcome(self):
        import csv
        real_writer = csv.writer
        def failing_writer(stream, **options):
            delegate = real_writer(stream, **options)
            class FailingWriter:
                def writerow(self, row):
                    if row[0] == "2":
                        raise OSError("disk write failure")
                    return delegate.writerow(row)
            return FailingWriter()
        with patch("experiments.p5_portable_core.core.csv.writer", side_effect=failing_writer), self.assertRaises(JobError):
            self.engine.run(self.job["id"])
        result = self.engine.recover()
        self.assertEqual(result["partial_evidence"], 1)
        job = self.engine.inspect(self.job["id"])
        self.assertEqual(job["state"], "FAILED")
        self.assertEqual(job["attempts"][0]["outcome"], "FAILED")
        self.assertEqual(job["artifacts"][0]["status"], "QUARANTINED")
        self.assert_repeat_is_idempotent()

    def test_unreadable_artifact_returns_safe_recovery_issue(self):
        self.engine.run(self.job["id"])
        with patch("experiments.p5_portable_core.core.checksum", side_effect=PermissionError("secret path")):
            result = self.engine.recover()
        self.assertEqual(result["issues"][0]["code"], "RECOVERY_UNREADABLE")
        self.assertTrue(result["issues"][0]["retryable"])
        self.assertNotIn("secret", json.dumps(result))
        self.assertEqual(self.engine.inspect(self.job["id"])["state"], "REVISION_REQUIRED")

    def test_unsafe_recovery_metadata_rolls_back(self):
        self.engine.run(self.job["id"])
        with sqlite3.connect(self.engine.db_path) as db:
            db.execute("UPDATE artifacts SET path='../synthetic.csv'")
        with self.assertRaises(JobError) as caught:
            self.engine.recover()
        self.assertEqual(caught.exception.code, "RECOVERY_PATH")
        self.assertEqual(self.source.read_bytes(), self.original)
        self.assertEqual(self.engine.inspect(self.job["id"])["state"], "REVIEW_REQUIRED")

    def test_failure_report_cannot_overwrite_already_committed_terminal_state(self):
        finish = self.engine._finish_transaction
        def ambiguous_response(*args):
            finish(*args)
            raise OSError("commit response lost")
        with patch.object(self.engine, "_finish_transaction", side_effect=ambiguous_response), self.assertRaises(JobError) as caught:
            self.engine.run(self.job["id"])
        self.assertEqual(caught.exception.code, "TERMINAL_STATE")
        job = self.engine.inspect(self.job["id"])
        self.assertEqual(job["state"], "REVIEW_REQUIRED")
        self.assertEqual(job["attempts"][0]["outcome"], "SUCCEEDED")
        self.assertEqual(job["artifacts"][0]["status"], "VERIFIED")

    def test_cli_recovery_reports_partial_evidence_with_nonzero_review_code(self):
        script = ("import os,sys; from experiments.p5_portable_core.core import Engine; "
                  "hook=lambda point,context: os._exit(23) if point=='row_written' else None; "
                  "Engine(sys.argv[1],fault_hook=hook).run(sys.argv[2])")
        child = subprocess.run([sys.executable, "-c", script, str(self.engine.root), self.job["id"]],
                               capture_output=True, text=True, timeout=10)
        self.assertEqual(child.returncode, 23)
        result = subprocess.run([sys.executable, "-m", "experiments.p5_portable_core",
                                 "--workspace", str(self.engine.root), "recover"],
                                capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 3, result.stderr)
        self.assertEqual(json.loads(result.stdout)["issues"][0]["code"], "RECOVERY_PARTIAL_OUTPUT")

    def test_terminal_storage_failure_remains_recoverable(self):
        with patch.object(self.engine, "_finish_transaction", side_effect=sqlite3.OperationalError("write failed")), self.assertRaises(JobError) as caught:
            self.engine.run(self.job["id"])
        self.assertEqual(caught.exception.code, "STATE_PERSISTENCE")
        self.assertTrue(caught.exception.retryable)
        self.assertEqual(self.engine.recover()["interrupted_attempts"], 1)
        job = self.engine.inspect(self.job["id"])
        self.assertEqual(job["state"], "INTERRUPTED")
        self.assertEqual(job["artifacts"][0]["status"], "QUARANTINED")

    def test_recovery_storage_failure_is_structured_and_retryable(self):
        class Crash(BaseException):
            pass
        self.engine.fault_hook = lambda point, context: (_ for _ in ()).throw(Crash()) if point == "attempt_started" else None
        with self.assertRaises(Crash):
            self.engine.run(self.job["id"])
        with patch.object(self.engine, "_event", side_effect=sqlite3.OperationalError("SECRET")), self.assertRaises(JobError) as caught:
            self.engine.recover()
        self.assertEqual(caught.exception.code, "RECOVERY_STORAGE")
        self.assertNotIn("SECRET", caught.exception.message)
        self.assertEqual(self.engine.inspect(self.job["id"])["state"], "RUNNING")
        self.assertEqual(self.engine.recover()["interrupted_attempts"], 1)

    def test_cancellation_at_each_finalization_boundary(self):
        for point in ("artifact_prepared", "output_published", "before_terminal_commit"):
            with self.subTest(point=point):
                job = self.engine.create(self.source)
                def hook(name, context):
                    if name == point:
                        self.engine.cancel(job["id"])
                self.engine.fault_hook = hook
                result = self.engine.run(job["id"])
                self.assertEqual(result["state"], "CANCELLED")
                self.assertTrue(all(a["status"] == "QUARANTINED" for a in result["artifacts"]))
                self.assertFalse(result["delivery_approved"])
        self.assertEqual(self.source.read_bytes(), self.original)

    def test_no_retroactive_failure_after_terminal_commit(self):
        def hook(point, context):
            if point == "terminal_committed":
                raise OSError("report channel failed")
        self.engine.fault_hook = hook
        with self.assertRaises(JobError) as caught:
            self.engine.run(self.job["id"])
        self.assertEqual(caught.exception.code, "POST_COMMIT_REPORT")
        self.assertEqual(self.engine.inspect(self.job["id"])["state"], "REVIEW_REQUIRED")

    def test_unsupported_schema_is_not_silently_overwritten(self):
        with sqlite3.connect(self.engine.db_path) as db:
            db.execute("PRAGMA user_version=999")
        with self.assertRaises(JobError) as caught:
            Engine(self.engine.root)
        self.assertEqual(caught.exception.code, "SCHEMA_VERSION")
        with sqlite3.connect(self.engine.db_path) as db:
            self.assertEqual(db.execute("PRAGMA user_version").fetchone()[0], 999)

    def test_version_one_migration_preserves_existing_jobs(self):
        # Build the old schema without touching the main test workspace.
        legacy = self.root / "legacy"
        legacy.mkdir()
        with sqlite3.connect(legacy / "jobs.sqlite3") as db:
            db.executescript("""
              CREATE TABLE jobs(id TEXT PRIMARY KEY,state TEXT,input_path TEXT,input_sha256 TEXT,
                cancel_requested INTEGER DEFAULT 0,created REAL,error_json TEXT);
              CREATE TABLE attempts(id TEXT PRIMARY KEY,job_id TEXT,phase TEXT,outcome TEXT,
                validation TEXT,review TEXT DEFAULT 'PENDING',started REAL,finished REAL,
                input_rows INTEGER DEFAULT 0,output_rows INTEGER DEFAULT 0);
              CREATE TABLE artifacts(id TEXT PRIMARY KEY,attempt_id TEXT,path TEXT UNIQUE,
                sha256 TEXT,bytes INTEGER,status TEXT);
              PRAGMA user_version=1;
              INSERT INTO jobs VALUES('old','READY','input.csv','legacy-digest',0,1,NULL);
            """)
        migrated = Engine(legacy)
        self.assertEqual(migrated.inspect("old")["state"], "READY")
        with sqlite3.connect(migrated.db_path) as db:
            self.assertEqual(db.execute("PRAGMA user_version").fetchone()[0], 2)
        self.assertEqual(Engine(legacy).inspect("old")["input_sha256"], "legacy-digest")


if __name__ == "__main__":
    unittest.main()
