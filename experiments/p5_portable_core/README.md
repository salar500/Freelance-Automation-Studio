# P5 portable core experiment

An executable Python **standard-library** experiment, authorized on 2026-10-12.
It is independent of the proposed Qt/.NET desktop stacks. Tested with the cloud's
existing CPython 3.12.14; no dependencies installed or downloaded.

From the repository root:

```bash
python -m experiments.p5_portable_core --workspace /tmp/fas-p5-demo process experiments/p5_portable_core/fixtures/duplicates.csv
```

The synthetic fixture has five records and two exact duplicates. The result has
three records in first-occurrence order. Progress is JSON on stderr; the final
job/attempt/artifact result is JSON on stdout. The output is **REVIEW_REQUIRED**,
never approved for client delivery. Use a fresh owned workspace outside the
repository; the above command creates another isolated job if run again.

```bash
python -m experiments.p5_portable_core --workspace /tmp/fas-p5-demo create experiments/p5_portable_core/fixtures/duplicates.csv
python -m experiments.p5_portable_core --workspace /tmp/fas-p5-demo run JOB_ID
python -m experiments.p5_portable_core --workspace /tmp/fas-p5-demo show JOB_ID
python -m experiments.p5_portable_core --workspace /tmp/fas-p5-demo verify JOB_ID
python -m experiments.p5_portable_core --workspace /tmp/fas-p5-demo cancel JOB_ID
python -m experiments.p5_portable_core --workspace /tmp/fas-p5-demo recover
```

Replace JOB_ID with the `id` returned by `create`. Cancellation may be requested
from another process while a job runs. For a reproducible demonstration, create
a fresh job and use `run JOB_ID --cancel-after-rows 1`. Exit codes: 0 success,
1 structured error, 2 cancelled, 3 recovery completed with issues requiring
review. Ctrl+C during processing requests termination
at the processing exception boundary and records cancellation when storage is
available. Process termination requires a subsequent explicit `recover`.

Run the actual unit/integration tests:

```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s experiments/p5_portable_core/tests -v
```

On Windows the environment-variable prefix is unnecessary; the equivalent
`python -m unittest ...` command is only a proposal, not Windows test evidence.

## Behavior and evidence

- SQLite persists jobs, attempts, artifact manifests and audit events. The
  experimental four-table schema is not an implementation of P3's full model.
- Job creation snapshots bytes without changing the original. Recorded SHA-256
  is checked before and after processing. Source changes after snapshot creation
  do not alter the saved job input.
- Accept UTF-8/UTF-8-BOM CSV with unique, nonempty headers and consistent row
  widths. Header-only files are valid. Malformed/oversized/invalid-encoding input
  fails with a stable, safe error code. Exact cell tuples are compared without
  trimming, fuzzy matching, formula execution or business interpretation.
- Preserve first occurrence and order; reconcile output headers/row count and
  record size/checksum. Outputs are staged, flushed and fsynced, then published
  with an exclusive hard link into a unique attempt directory. Existing
  destinations are never intentionally overwritten.
- Database PREPARED metadata precedes publication; failed/interrupted artifacts
  are QUARANTINED. Evidence/partial files are retained, not silently cleaned.
  Database and filesystem are **not** one atomic transaction.
- Schema version 2 journals intended staging/final paths before writing. Additive
  migration preserves version-1 jobs and artifacts; unknown schema versions are
  rejected instead of silently rewritten. Terminal outcome, validation and
  verified artifact eligibility commit together. A later reporting/storage error
  cannot rewrite an already terminal attempt.
- Recovery observes filesystem hashes/sizes, records observations durably and
  indexes partial bytes as quarantined evidence. Missing/tampered/unreadable
  previously verified output loses eligibility and requires revision; recovery
  does not automatically restore quarantined artifacts or grant approval.
  Failed/cancelled write remnants are indexed without rewriting their outcomes.
  Repeated recovery creates no duplicate artifacts/events for reconciled attempts.
- OS workspace locks serialize execution/recovery and release on process exit.
  Cancellation uses SQLite and remains available during execution. Recovery
  refuses to run while an execution owns the lock.
- Explicit retries of failed/cancelled/interrupted jobs create new attempts and
  retain old outcomes. Successful jobs cannot silently re-execute.
- Successful processing, validation, review and delivery approval are distinct.
  `verify` detects altered/missing outputs and removes artifact eligibility.
  No approval/export/client-delivery function exists.

Managed data layout (outside the repository):

```text
WORKSPACE/jobs.sqlite3
WORKSPACE/.execution.lock
WORKSPACE/jobs/JOB_ID/input.csv
WORKSPACE/jobs/JOB_ID/attempts/ATTEMPT_ID/output.partial.csv
WORKSPACE/jobs/JOB_ID/attempts/ATTEMPT_ID/output.csv
```

## Limits and pending work

Use synthetic data only. Default experimental bounds are 32 MiB input and
100,000 records; they are safety limits, not measured performance guarantees.
Deduplication keeps unique rows in memory and persists progress per record.
UTF-8 field limits also follow the installed Python CSV parser's defaults.
CSV formulas are preserved as text; opening them in a spreadsheet could execute
formulas. This experiment does not provide formula-safe client export.

The workspace must be trusted and use a local filesystem supporting hard links.
File locks/path checks are not a security sandbox or protection against an
attacker running as the same user. Power-loss durability, directory fsync,
symlink race confinement, network filesystems and corrupted-database repair
are not proven. A database/storage failure may prevent failure-state recording;
the CLI reports an error and recovery must reconcile later. Incomplete creation
may leave an unregistered snapshot directory for manual evidence review.

## Crash-consistency verification

The original 29 tests are preserved, with 21 additional tests in
`tests/test_crash_consistency.py`. Run only the new tests with:

```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s experiments/p5_portable_core/tests -p test_crash_consistency.py -v
```

Trusted test code may supply an `Engine(..., fault_hook=callback)`. This callback
is never parsed from imported configuration or exposed as a CLI job setting.
Named checkpoints: `attempt_started`, `row_written`, `staging_written`,
`artifact_prepared`, `output_published`, `before_terminal_commit`,
`terminal_committed`. Tests terminate a subprocess with `os._exit` at exact
checkpoints; no timing-based sleeps are required. Additional cases cover
simulated disk/write/fsync/DB failures, cancellation during finalization,
missing/tampered/unreadable files, unsafe metadata, migration and idempotency.

POSIX directory entries are fsynced after staging/publication/unlink; Windows
directory durability is not verified and that branch does not claim equivalent
flush behavior. Recovery preserves ambiguous evidence instead of automatically
renaming/removing files. Quarantined unreadable output stays ineligible even
after access is restored; review or an explicitly authorized correction is
needed. Legacy attempts without recorded paths may have incomplete evidence.
Host/filesystem/device behavior under physical power loss remains unproven.

The Linux implementation is tested; the Windows `msvcrt` lock branch, native
GUI, installer, full dependency/license clearance and performance budgets remain
pending. No production architecture ADR is approved. The 239 previously planned
product acceptance cases remain distinct from these executed prototype tests.

Governance/evidence: [P5 milestone report](../../docs/milestone-reports/MS-0006-P5.md).
