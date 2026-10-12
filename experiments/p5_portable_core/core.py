"""Local CSV jobs with durable evidence; no GUI or production architecture claim."""

from contextlib import closing, contextmanager
import csv
import hashlib
import json
import math
import os
from pathlib import Path
import sqlite3
import shutil
import sys
import time
import uuid


class JobError(Exception):
    """A stable, user-safe failure contract; never includes raw client content."""

    def __init__(self, code, message, *, retryable=False):
        super().__init__(message)
        self.code = code
        self.message = message
        self.retryable = retryable

    def as_dict(self):
        return {"code": self.code, "message": self.message,
                "retryable": self.retryable}


def checksum(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(262144), b""):
            digest.update(chunk)
    return digest.hexdigest()


class _Cancelled(Exception):
    pass


SCHEMA = """
CREATE TABLE IF NOT EXISTS jobs (
 id TEXT PRIMARY KEY, state TEXT NOT NULL, input_path TEXT NOT NULL,
 input_sha256 TEXT NOT NULL, cancel_requested INTEGER NOT NULL DEFAULT 0,
 created REAL NOT NULL, error_json TEXT
);
CREATE TABLE IF NOT EXISTS attempts (
 id TEXT PRIMARY KEY, job_id TEXT NOT NULL REFERENCES jobs(id),
 phase TEXT NOT NULL, outcome TEXT NOT NULL, validation TEXT NOT NULL,
 review TEXT NOT NULL DEFAULT 'PENDING', started REAL NOT NULL, finished REAL,
 input_rows INTEGER NOT NULL DEFAULT 0, output_rows INTEGER NOT NULL DEFAULT 0,
 staging_path TEXT, final_path TEXT, recovery_json TEXT
);
CREATE TABLE IF NOT EXISTS artifacts (
 id TEXT PRIMARY KEY, attempt_id TEXT NOT NULL REFERENCES attempts(id),
 path TEXT NOT NULL UNIQUE, sha256 TEXT NOT NULL, bytes INTEGER NOT NULL,
 status TEXT NOT NULL, recovery_json TEXT
);
CREATE TABLE IF NOT EXISTS events (
 id INTEGER PRIMARY KEY, job_id TEXT NOT NULL REFERENCES jobs(id),
 attempt_id TEXT, timestamp REAL NOT NULL, kind TEXT NOT NULL, data TEXT NOT NULL
);
"""


class Engine:
    """Single execution coordinator; cancellation may arrive from another process.

    Workspaces must be trusted local directories. Locks provide crash/concurrency
    coordination, not a sandbox against other software running as the same user.
    """

    def __init__(self, workspace, *, max_input_bytes=32 * 1024 * 1024,
                 max_rows=100_000, fault_hook=None, checkpoint_rows=100,
                 max_field_chars=131_072, max_columns=256,
                 max_unique_memory_bytes=64 * 1024 * 1024,
                 min_free_bytes=16 * 1024 * 1024, timeout_seconds=30):
        integers = (max_input_bytes, max_rows, checkpoint_rows, max_field_chars,
                    max_columns, max_unique_memory_bytes)
        if any(not isinstance(n, int) or isinstance(n, bool) or n <= 0 for n in integers):
            raise JobError("RESOURCE_CONFIG", "Resource limits must be positive integers.")
        if not isinstance(min_free_bytes, int) or min_free_bytes < 0:
            raise JobError("RESOURCE_CONFIG", "Free-space reserve must be nonnegative.")
        if not math.isfinite(timeout_seconds) or timeout_seconds <= 0:
            raise JobError("RESOURCE_CONFIG", "Processing deadline must be finite and positive.")
        root = Path(workspace).absolute()
        if root.is_symlink():
            raise JobError("UNSAFE_WORKSPACE", "Workspace must not be a symbolic link.")
        self.root = root.resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        self.db_path = self.root / "jobs.sqlite3"
        self.max_input_bytes = max_input_bytes
        self.max_rows = max_rows
        self.checkpoint_rows = checkpoint_rows
        self.max_field_chars = min(max_field_chars, csv.field_size_limit())
        self.max_columns = max_columns
        self.max_unique_memory_bytes = max_unique_memory_bytes
        self.min_free_bytes = min_free_bytes
        self.timeout_seconds = timeout_seconds
        self.fault_hook = fault_hook  # Trusted test code only; never loaded from job configuration.
        with self._db() as db:
            version = db.execute("PRAGMA user_version").fetchone()[0]
            if version not in {0, 1, 2}:
                raise JobError("SCHEMA_VERSION", "Workspace schema version is unsupported.")
            db.executescript(SCHEMA)
            # Additive, restart-safe migration of existing prototype workspaces.
            for table, columns in {"attempts": ("staging_path", "final_path", "recovery_json"),
                                   "artifacts": ("recovery_json",)}.items():
                existing = {row["name"] for row in db.execute(f"PRAGMA table_info({table})")}
                for column in columns:
                    if column not in existing:
                        db.execute(f"ALTER TABLE {table} ADD COLUMN {column} TEXT")
            db.execute("PRAGMA user_version = 2")

    def _checkpoint(self, name, **context):
        if self.fault_hook:
            self.fault_hook(name, context)

    def _check_disk(self, required_bytes):
        if shutil.disk_usage(self.root).free < required_bytes + self.min_free_bytes:
            raise JobError("RESOURCE_DISK", "Workspace free-space reserve is insufficient.", retryable=True)

    @staticmethod
    def _check_deadline(deadline):
        if time.monotonic() >= deadline:
            raise JobError("RESOURCE_TIMEOUT", "Experimental processing deadline exceeded.", retryable=True)

    def _persist_progress(self, attempt_id, count, kept):
        try:
            with self._db() as db:
                db.execute("UPDATE attempts SET input_rows=?,output_rows=? WHERE id=?", (count, kept, attempt_id))
        except (sqlite3.Error, OSError):
            raise JobError("STATE_PERSISTENCE", "Progress could not be saved; run recovery.", retryable=True) from None

    @staticmethod
    def _sync_directory(path):
        # Windows directory flush semantics need native verification; don't pretend
        # POSIX directory fsync is portable or proves physical power-loss survival.
        if os.name != "nt":
            descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
            try:
                os.fsync(descriptor)
            finally:
                os.close(descriptor)

    @contextmanager
    def _db(self):
        with closing(sqlite3.connect(self.db_path, timeout=5)) as db:
            db.row_factory = sqlite3.Row
            db.execute("PRAGMA foreign_keys = ON")
            with db:
                yield db

    @contextmanager
    def _execution_lock(self):
        # OS locks are released even when the coordinator process crashes.
        with (self.root / ".execution.lock").open("a+b") as stream:
            locked = False
            try:
                if os.name == "nt":
                    import msvcrt
                    if stream.seek(0, 2) == 0:
                        stream.write(b"0")
                        stream.flush()
                    stream.seek(0)
                    try:
                        msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
                    except OSError:
                        raise JobError("BUSY", "Another execution owns this workspace.") from None
                else:
                    import fcntl
                    try:
                        fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                    except BlockingIOError:
                        raise JobError("BUSY", "Another execution owns this workspace.") from None
                locked = True
                yield
            finally:
                if locked:
                    if os.name == "nt":
                        stream.seek(0)
                        msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
                    else:
                        fcntl.flock(stream.fileno(), fcntl.LOCK_UN)

    def _path(self, relative):
        path = self.root / relative
        if not path.resolve().is_relative_to(self.root):
            raise JobError("UNSAFE_PATH", "Managed path escapes the workspace.")
        return path

    @staticmethod
    def _event(db, job_id, attempt_id, kind, data):
        db.execute("INSERT INTO events(job_id,attempt_id,timestamp,kind,data) VALUES(?,?,?,?,?)",
                   (job_id, attempt_id, time.time(), kind, json.dumps(data, sort_keys=True)))

    def create(self, input_file):
        source = Path(input_file)
        if not source.is_file():
            raise JobError("INPUT_MISSING", "Input file does not exist.")
        if source.stat().st_size > self.max_input_bytes:
            raise JobError("INPUT_TOO_LARGE", "Input exceeds the experimental size limit.")
        self._check_disk(source.stat().st_size)
        job_id = uuid.uuid4().hex
        folder = self._path(f"jobs/{job_id}")
        folder.mkdir(parents=True, exist_ok=False)
        snapshot = folder / "input.csv"
        before = checksum(source)
        with source.open("rb") as inp, snapshot.open("xb") as out:
            total = 0
            while chunk := inp.read(262144):
                total += len(chunk)
                if total > self.max_input_bytes:
                    raise JobError("INPUT_TOO_LARGE", "Input grew beyond the experimental limit.")
                out.write(chunk)
            out.flush()
            os.fsync(out.fileno())
        if checksum(source) != before or checksum(snapshot) != before:
            raise JobError("INPUT_CHANGED", "Input changed while its snapshot was created.")
        relative = str(snapshot.relative_to(self.root))
        with self._db() as db:
            db.execute("INSERT INTO jobs(id,state,input_path,input_sha256,created) VALUES(?,?,?,?,?)",
                       (job_id, "DRAFT", relative, before, time.time()))
            self._event(db, job_id, None, "CREATED", {"input_sha256": before})
            db.execute("UPDATE jobs SET state='READY' WHERE id=?", (job_id,))
            self._event(db, job_id, None, "READY", {})
        return self.inspect(job_id)

    def inspect(self, job_id):
        with self._db() as db:
            job = db.execute("SELECT * FROM jobs WHERE id=?", (job_id,)).fetchone()
            if job is None:
                raise JobError("JOB_NOT_FOUND", "Job does not exist.")
            result = dict(job)
            result["attempts"] = [dict(row) for row in db.execute(
                "SELECT * FROM attempts WHERE job_id=? ORDER BY started,id", (job_id,))]
            result["artifacts"] = [dict(row) for row in db.execute(
                "SELECT artifacts.* FROM artifacts JOIN attempts ON attempt_id=attempts.id "
                "WHERE job_id=? ORDER BY artifacts.id", (job_id,))]
            result["error"] = json.loads(result.pop("error_json") or "null")
            for item in result["attempts"] + result["artifacts"]:
                item["recovery"] = json.loads(item.pop("recovery_json") or "null")
            result["delivery_approved"] = False  # No delivery approval API in this experiment.
            return result

    def cancel(self, job_id):
        with self._db() as db:
            job = db.execute("SELECT state FROM jobs WHERE id=?", (job_id,)).fetchone()
            if job is None:
                raise JobError("JOB_NOT_FOUND", "Job does not exist.")
            if job["state"] not in {"READY", "RUNNING", "VALIDATING"}:
                raise JobError("INVALID_STATE", "Job cannot be cancelled in its current state.")
            db.execute("UPDATE jobs SET cancel_requested=1 WHERE id=?", (job_id,))
            self._event(db, job_id, None, "CANCEL_REQUESTED", {})

    def _check_cancel(self, job_id, connection=None):
        if connection is None:
            with self._db() as db:
                row = db.execute("SELECT cancel_requested FROM jobs WHERE id=?", (job_id,)).fetchone()
        else:
            row = connection.execute("SELECT cancel_requested FROM jobs WHERE id=?", (job_id,)).fetchone()
        if row[0]:
            raise _Cancelled()

    def _finish(self, job_id, attempt_id, outcome, validation, error=None):
        try:
            self._finish_transaction(job_id, attempt_id, outcome, validation, error)
        except (sqlite3.Error, OSError):
            raise JobError("STATE_PERSISTENCE", "Terminal state could not be saved; run recovery.",
                           retryable=True) from None

    def _finish_transaction(self, job_id, attempt_id, outcome, validation, error):
        with self._db() as db:
            db.execute("BEGIN IMMEDIATE")
            if db.execute("SELECT phase FROM attempts WHERE id=?", (attempt_id,)).fetchone()[0] == "FINISHED":
                raise JobError("TERMINAL_STATE", "Attempt already finalized; inspect its saved outcome.")
            if outcome == "SUCCEEDED" and db.execute(
                    "SELECT cancel_requested FROM jobs WHERE id=?", (job_id,)).fetchone()[0]:
                outcome, validation = "CANCELLED", "NOT_RUN"
            state = "REVIEW_REQUIRED" if outcome == "SUCCEEDED" else outcome
            db.execute("UPDATE attempts SET phase='FINISHED',outcome=?,validation=?,finished=? WHERE id=?",
                       (outcome, validation, time.time(), attempt_id))
            db.execute("UPDATE jobs SET state=?,error_json=? WHERE id=?",
                       (state, json.dumps(error.as_dict()) if error else None, job_id))
            if outcome != "SUCCEEDED":
                db.execute("UPDATE artifacts SET status='QUARANTINED' WHERE attempt_id=?", (attempt_id,))
            else:
                # Eligibility, outcome and job state commit in the same transaction.
                db.execute("UPDATE artifacts SET status='VERIFIED' WHERE attempt_id=?", (attempt_id,))
            self._event(db, job_id, attempt_id, "FINISHED", {"outcome": outcome, "validation": validation})

    def run(self, job_id, progress=None):
        """Exact row deduplication, keeping first occurrence and input order."""
        with self._execution_lock():
            job = self.inspect(job_id)
            if job["state"] not in {"READY", "FAILED", "CANCELLED", "INTERRUPTED"}:
                raise JobError("INVALID_STATE", "Job cannot execute in its current state.")
            attempt_id = uuid.uuid4().hex
            folder = self._path(f"jobs/{job_id}/attempts/{attempt_id}")
            folder.mkdir(parents=True, exist_ok=False)
            staging = folder / "output.partial.csv"
            final = folder / "output.csv"
            with self._db() as db:
                # Retry is explicit; a READY pre-start cancellation remains effective.
                if job["state"] != "READY":
                    db.execute("UPDATE jobs SET cancel_requested=0,error_json=NULL WHERE id=?", (job_id,))
                db.execute("INSERT INTO attempts(id,job_id,phase,outcome,validation,started,staging_path,final_path) "
                           "VALUES(?,?,?,?,?,?,?,?)", (attempt_id, job_id, "PREFLIGHT", "PENDING", "NOT_RUN",
                           time.time(), str(staging.relative_to(self.root)), str(final.relative_to(self.root))))
                db.execute("UPDATE jobs SET state='RUNNING' WHERE id=?", (job_id,))
                self._event(db, job_id, attempt_id, "STARTED", {})
            count = kept = 0
            committed = False
            deadline = time.monotonic() + self.timeout_seconds
            try:
                self._checkpoint("attempt_started", job_id=job_id, attempt_id=attempt_id)
                self._check_cancel(job_id)
                source = self._path(job["input_path"])
                self._check_disk(source.stat().st_size * 2)
                self._check_deadline(deadline)
                if checksum(source) != job["input_sha256"]:
                    raise JobError("INPUT_INTEGRITY", "The input snapshot has changed.")
                with self._db() as db:
                    db.execute("UPDATE attempts SET phase='RUNNING' WHERE id=?", (attempt_id,))
                seen = set()
                unique_storage = 0
                # Reuse a read-only cancellation connection. It never holds a write
                # transaction across callbacks; other processes can still cancel.
                with self._db() as control, source.open("r", encoding="utf-8-sig", newline="") as inp, staging.open(
                        "x", encoding="utf-8", newline="") as out:
                    reader = csv.reader(inp, strict=True)
                    writer = csv.writer(out, lineterminator="\n")
                    headers = next(reader, None)
                    if not headers or any(not h.strip() for h in headers) or len(set(headers)) != len(headers):
                        raise JobError("INPUT_HEADERS", "CSV requires nonempty, unique column headers.")
                    if len(headers) > self.max_columns:
                        raise JobError("COLUMN_LIMIT", "CSV exceeds the experimental column limit.")
                    if any(len(h) > self.max_field_chars for h in headers):
                        raise JobError("FIELD_LIMIT", "CSV field exceeds the experimental character limit.")
                    writer.writerow(headers)
                    for row in reader:
                        self._check_cancel(job_id, control)
                        self._check_deadline(deadline)
                        count += 1
                        if count > self.max_rows:
                            raise JobError("ROW_LIMIT", "Input exceeds the experimental row limit.")
                        if len(row) != len(headers):
                            raise JobError("INPUT_SCHEMA", "CSV row width does not match its headers.")
                        if any(len(cell) > self.max_field_chars for cell in row):
                            raise JobError("FIELD_LIMIT", "CSV field exceeds the experimental character limit.")
                        key = tuple(row)
                        if key not in seen:
                            seen.add(key)
                            unique_storage += sys.getsizeof(key) + sum(sys.getsizeof(cell) for cell in key)
                            if unique_storage + sys.getsizeof(seen) > self.max_unique_memory_bytes:
                                raise JobError("RESOURCE_MEMORY", "Unique-row memory estimate exceeds the experimental budget.")
                            writer.writerow(row)
                            kept += 1
                        if self.fault_hook:
                            out.flush()
                        self._checkpoint("row_written", job_id=job_id, attempt_id=attempt_id)
                        if count % self.checkpoint_rows == 0:
                            self._persist_progress(attempt_id, count, kept)
                            self._check_disk(0)
                        if progress:
                            progress({"job_id": job_id, "attempt_id": attempt_id, "phase": "RUNNING",
                                      "input_rows": count, "output_rows": kept, "duplicates": count-kept})
                    self._persist_progress(attempt_id, count, kept)
                    out.flush()
                    os.fsync(out.fileno())
                self._sync_directory(folder)
                self._checkpoint("staging_written", job_id=job_id, attempt_id=attempt_id)
                self._check_cancel(job_id)
                self._check_deadline(deadline)
                with self._db() as db:
                    db.execute("UPDATE jobs SET state='VALIDATING' WHERE id=?", (job_id,))
                    db.execute("UPDATE attempts SET phase='VALIDATING' WHERE id=?", (attempt_id,))
                with staging.open(encoding="utf-8", newline="") as output:
                    check = csv.reader(output, strict=True)
                    if next(check) != headers or sum(1 for _ in check) != kept:
                        raise JobError("OUTPUT_VALIDATION", "Output reconciliation failed.")
                if checksum(source) != job["input_sha256"]:
                    raise JobError("INPUT_INTEGRITY", "Input snapshot changed during processing.")
                digest = checksum(staging)
                self._check_deadline(deadline)
                artifact_id = uuid.uuid4().hex
                with self._db() as db:
                    db.execute("INSERT INTO artifacts(id,attempt_id,path,sha256,bytes,status) VALUES(?,?,?,?,?,?)", (artifact_id, attempt_id,
                               str(final.relative_to(self.root)), digest, staging.stat().st_size, "PREPARED"))
                    self._event(db, job_id, attempt_id, "ARTIFACT_PREPARED", {"sha256": digest})
                self._checkpoint("artifact_prepared", job_id=job_id, attempt_id=attempt_id)
                self._check_cancel(job_id)
                # Same-filesystem hard link publishes complete bytes without overwriting a destination.
                os.link(staging, final)
                self._sync_directory(folder)
                self._checkpoint("output_published", job_id=job_id, attempt_id=attempt_id)
                staging.unlink()
                self._sync_directory(folder)
                if checksum(final) != digest:
                    raise JobError("OUTPUT_INTEGRITY", "Published output checksum does not match.")
                self._check_cancel(job_id)
                self._checkpoint("before_terminal_commit", job_id=job_id, attempt_id=attempt_id)
                self._check_deadline(deadline)
                self._finish(job_id, attempt_id, "SUCCEEDED", "PASSED")
                committed = True
                self._checkpoint("terminal_committed", job_id=job_id, attempt_id=attempt_id)
                # Return the committed terminal result; don't let a reporting callback
                # retroactively turn a terminal success into a processing failure.
                return self.inspect(job_id)
            except (_Cancelled, KeyboardInterrupt):
                if committed:
                    return self.inspect(job_id)
                self._persist_progress(attempt_id, count, kept)
                self._finish(job_id, attempt_id, "CANCELLED", "NOT_RUN")
                return self.inspect(job_id)
            except (JobError, UnicodeError, csv.Error, OSError, sqlite3.Error) as exc:
                if committed:
                    raise JobError("POST_COMMIT_REPORT", "Execution committed; inspect its saved result.") from None
                if isinstance(exc, JobError):
                    error = exc
                elif isinstance(exc, UnicodeError):
                    error = JobError("INPUT_ENCODING", "CSV must use valid UTF-8 encoding.")
                elif isinstance(exc, csv.Error):
                    error = JobError("FIELD_LIMIT", "CSV field exceeds the parser character limit.") if "field larger than field limit" in str(exc) else JobError("INPUT_CSV", "CSV syntax is unsupported.")
                else:
                    error = JobError("STORAGE_ERROR", "Local storage operation failed.", retryable=True)
                self._persist_progress(attempt_id, count, kept)
                self._finish(job_id, attempt_id, "FAILED", "FAILED", error)
                raise error from None
            except MemoryError:
                error = JobError("RESOURCE_MEMORY", "Experimental memory allocation failed.")
                self._finish(job_id, attempt_id, "FAILED", "FAILED", error)
                raise error from None
            except Exception:
                if committed:
                    raise JobError("POST_COMMIT_REPORT", "Execution committed; inspect its saved result.") from None
                error = JobError("INTERNAL_ERROR", "Unexpected processing failure; review diagnostic evidence.")
                self._persist_progress(attempt_id, count, kept)
                self._finish(job_id, attempt_id, "FAILED", "FAILED", error)
                raise error from None

    def _observe(self, relative, expected_sha256=None, expected_bytes=None):
        if relative is None:
            return {"state": "NOT_RECORDED"}
        path = self._path(relative)
        try:
            if not path.exists():
                return {"state": "MISSING"}
            if not path.is_file():
                return {"state": "UNSAFE_TYPE"}
            size = path.stat().st_size
            if size > self.max_input_bytes * 2:
                return {"state": "OVERSIZED", "bytes": size}
            digest = checksum(path)
            state = "UNVERIFIED" if expected_sha256 is None else "MATCH"
            if expected_sha256 is not None and (digest != expected_sha256 or size != expected_bytes):
                state = "TAMPERED"
            return {"state": state, "bytes": size, "sha256": digest}
        except OSError:
            return {"state": "UNREADABLE"}

    def recover(self):
        """Reconcile filesystem evidence without promoting uncertain artifacts."""
        try:
            return self._recover_transaction()
        except (sqlite3.Error, OSError):
            raise JobError("RECOVERY_STORAGE", "Recovery could not be saved; preserve evidence and retry.",
                           retryable=True) from None
        except JobError as exc:
            if exc.code == "UNSAFE_PATH":
                raise JobError("RECOVERY_PATH", "Recovery metadata contains an unsafe managed path.") from None
            raise

    def _recover_transaction(self):
        with self._execution_lock(), self._db() as db:
            db.execute("BEGIN IMMEDIATE")
            rows = db.execute("SELECT * FROM attempts WHERE phase!='FINISHED'").fetchall()
            issues = []
            for row in rows:
                artifact = db.execute("SELECT * FROM artifacts WHERE attempt_id=?", (row["id"],)).fetchone()
                final_path = row["final_path"] or (artifact["path"] if artifact else None)
                staging_path = row["staging_path"]
                if staging_path is None and final_path:
                    staging_path = str(Path(final_path).with_name("output.partial.csv"))
                expected = artifact["sha256"] if artifact else None
                size = artifact["bytes"] if artifact else None
                observation = {"staging": self._observe(staging_path, expected, size),
                               "final": self._observe(final_path, expected, size)}
                details = json.dumps(observation, sort_keys=True)
                if artifact:
                    db.execute("UPDATE artifacts SET status='QUARANTINED',recovery_json=? WHERE id=?",
                               (details, artifact["id"]))
                    if all(item["state"] == "MISSING" for item in observation.values()):
                        issues.append({"job_id": row["job_id"], "code": "RECOVERY_MISSING", "retryable": False})
                elif observation["staging"]["state"] == "UNVERIFIED":
                    # Preserve partial bytes as quarantined evidence, never as eligible output.
                    db.execute("INSERT INTO artifacts(id,attempt_id,path,sha256,bytes,status,recovery_json) "
                               "VALUES(?,?,?,?,?,?,?)", (uuid.uuid4().hex, row["id"], staging_path,
                               observation["staging"]["sha256"], observation["staging"]["bytes"],
                               "QUARANTINED", details))
                    issues.append({"job_id": row["job_id"], "code": "RECOVERY_PARTIAL_OUTPUT", "retryable": False})
                for evidence in observation.values():
                    if evidence["state"] in {"TAMPERED", "UNREADABLE", "UNSAFE_TYPE", "OVERSIZED"}:
                        issues.append({"job_id": row["job_id"], "code": "RECOVERY_" + evidence["state"],
                                       "retryable": evidence["state"] == "UNREADABLE"})
                db.execute("UPDATE attempts SET phase='FINISHED',outcome='INTERRUPTED',"
                           "validation='NOT_RUN',finished=?,recovery_json=? WHERE id=?",
                           (time.time(), details, row["id"]))
                db.execute("UPDATE jobs SET state='INTERRUPTED' WHERE id=?", (row["job_id"],))
                db.execute("UPDATE artifacts SET status='QUARANTINED' WHERE attempt_id=?", (row["id"],))
                self._event(db, row["job_id"], row["id"], "RECOVERED_INTERRUPTION", observation)
            partial_evidence = 0
            # Ordinary write errors/cancellation can leave partial bytes too. Index
            # them once without changing the truthful terminal attempt outcome.
            terminal = db.execute("SELECT * FROM attempts WHERE phase='FINISHED' "
                                  "AND outcome IN ('FAILED','CANCELLED') AND recovery_json IS NULL").fetchall()
            for row in terminal:
                artifact = db.execute("SELECT * FROM artifacts WHERE attempt_id=?", (row["id"],)).fetchone()
                expected = artifact["sha256"] if artifact else None
                size = artifact["bytes"] if artifact else None
                observed = {"staging": self._observe(row["staging_path"], expected, size),
                            "final": self._observe(row["final_path"], expected, size)}
                details = json.dumps(observed, sort_keys=True)
                db.execute("UPDATE attempts SET recovery_json=? WHERE id=?", (details, row["id"]))
                if artifact:
                    db.execute("UPDATE artifacts SET recovery_json=? WHERE id=?", (details, artifact["id"]))
                elif observed["staging"]["state"] == "UNVERIFIED":
                    db.execute("INSERT INTO artifacts(id,attempt_id,path,sha256,bytes,status,recovery_json) "
                               "VALUES(?,?,?,?,?,?,?)", (uuid.uuid4().hex, row["id"], row["staging_path"],
                               observed["staging"]["sha256"], observed["staging"]["bytes"],
                               "QUARANTINED", details))
                    partial_evidence += 1
                    issues.append({"job_id": row["job_id"], "code": "RECOVERY_PARTIAL_OUTPUT", "retryable": False})
                for evidence in observed.values():
                    if evidence["state"] in {"TAMPERED", "UNREADABLE", "UNSAFE_TYPE", "OVERSIZED"}:
                        issues.append({"job_id": row["job_id"], "code": "RECOVERY_" + evidence["state"],
                                       "retryable": evidence["state"] == "UNREADABLE"})
                self._event(db, row["job_id"], row["id"], "RECOVERED_TERMINAL_EVIDENCE", observed)
            invalidated = 0
            for artifact in db.execute("SELECT artifacts.*,attempts.job_id FROM artifacts JOIN attempts "
                                       "ON attempts.id=attempt_id WHERE status='VERIFIED'").fetchall():
                observed = self._observe(artifact["path"], artifact["sha256"], artifact["bytes"])
                if observed["state"] == "MATCH":
                    continue
                invalidated += 1
                db.execute("UPDATE artifacts SET status='QUARANTINED',recovery_json=? WHERE id=?",
                           (json.dumps(observed, sort_keys=True), artifact["id"]))
                db.execute("UPDATE attempts SET validation='FAILED' WHERE id=?", (artifact["attempt_id"],))
                db.execute("UPDATE jobs SET state='REVISION_REQUIRED' WHERE id=?", (artifact["job_id"],))
                self._event(db, artifact["job_id"], artifact["attempt_id"], "RECOVERY_INTEGRITY_FAILED", observed)
                issues.append({"job_id": artifact["job_id"], "code": "RECOVERY_" + observed["state"],
                               "retryable": observed["state"] == "UNREADABLE"})
            return {"interrupted_attempts": len(rows), "job_ids": [row["job_id"] for row in rows],
                    "invalidated_artifacts": invalidated, "partial_evidence": partial_evidence, "issues": issues}

    def verify(self, job_id):
        with self._execution_lock():
            job = self.inspect(job_id)
            artifacts = [a for a in job["artifacts"] if a["status"] == "VERIFIED"]
            failures = []
            for artifact in artifacts:
                observed = self._observe(artifact["path"], artifact["sha256"], artifact["bytes"])
                if observed["state"] != "MATCH":
                    failures.append(artifact["id"])
            if failures:
                with self._db() as db:
                    for artifact_id in failures:
                        db.execute("UPDATE artifacts SET status='QUARANTINED' WHERE id=?", (artifact_id,))
                        db.execute("UPDATE attempts SET validation='FAILED' WHERE id="
                                   "(SELECT attempt_id FROM artifacts WHERE id=?)", (artifact_id,))
                    db.execute("UPDATE jobs SET state='REVISION_REQUIRED' WHERE id=?", (job_id,))
                    self._event(db, job_id, None, "ARTIFACT_INTEGRITY_FAILED", {"count": len(failures)})
                raise JobError("OUTPUT_INTEGRITY", "Stored output is missing or has changed.")
            if not artifacts:
                raise JobError("NO_VERIFIED_OUTPUT", "Job has no verified output.")
            return {"job_id": job_id, "artifacts_verified": len(artifacts), "delivery_approved": False}
