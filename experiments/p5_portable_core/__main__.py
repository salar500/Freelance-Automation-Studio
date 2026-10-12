"""Run with python -m experiments.p5_portable_core --workspace PATH COMMAND."""

import argparse
import json
import sqlite3
import sys

from .core import Engine, JobError


def progress_reporter(engine, job_id, cancel_after=None):
    """Bound CLI log volume without delaying the cancellation request."""
    cancel_sent = False
    def report(event):
        nonlocal cancel_sent
        rows = event["input_rows"]
        if cancel_after is not None and rows >= cancel_after and not cancel_sent:
            engine.cancel(job_id)
            cancel_sent = True
        if rows == 1 or rows % 100 == 0:
            print(json.dumps({"progress": event}, sort_keys=True), file=sys.stderr, flush=True)
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description="P5 local CSV core experiment (no client delivery)")
    parser.add_argument("--workspace", required=True, help="Owned local data directory outside source control")
    commands = parser.add_subparsers(dest="command", required=True)
    create = commands.add_parser("create")
    create.add_argument("input")
    commands.add_parser("process", help="Create and run one local CSV job").add_argument("input")
    run = commands.add_parser("run")
    run.add_argument("job_id")
    run.add_argument("--cancel-after-rows", type=int, help="Deterministic synthetic cancellation demonstration")
    for name in ("show", "cancel", "verify"):
        commands.add_parser(name).add_argument("job_id")
    commands.add_parser("recover")
    args = parser.parse_args(argv)
    if args.command == "run" and args.cancel_after_rows is not None and args.cancel_after_rows <= 0:
        parser.error("--cancel-after-rows must be positive")
    try:
        engine = Engine(args.workspace)
        if args.command == "create":
            result = engine.create(args.input)
        elif args.command == "process":
            job = engine.create(args.input)
            result = engine.run(job["id"], progress_reporter(engine, job["id"]))
        elif args.command == "run":
            result = engine.run(args.job_id, progress_reporter(engine, args.job_id, args.cancel_after_rows))
        elif args.command == "show":
            result = engine.inspect(args.job_id)
        elif args.command == "cancel":
            engine.cancel(args.job_id)
            result = engine.inspect(args.job_id)
        elif args.command == "verify":
            result = engine.verify(args.job_id)
        else:
            result = engine.recover()
        print(json.dumps(result, sort_keys=True))
        if args.command == "recover" and result.get("issues"):
            return 3  # Reconciliation ran, but quarantined/integrity issues need review.
        return 2 if result.get("state") == "CANCELLED" else 0
    except JobError as exc:
        print(json.dumps({"error": exc.as_dict()}, sort_keys=True), file=sys.stderr)
        return 1
    except (OSError, sqlite3.Error):
        print(json.dumps({"error": {"code": "STORAGE_ERROR", "message": "Local storage operation failed.",
                                    "retryable": True}}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
