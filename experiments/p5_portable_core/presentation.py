"""Experimental local presentation adapter; no production UI/framework adoption."""
import argparse
import json
from pathlib import Path
import shlex
import sqlite3
import threading

from .core import Engine, JobError


class JobService:
    """Application boundary: presentation never executes commands or writes SQL."""
    def __init__(self, workspace, **limits):
        self.engine = Engine(workspace, **limits)

    def create(self, source):
        path = Path(source)
        if path.suffix.lower() != '.csv':
            raise JobError('INPUT_FORMAT', 'Select a synthetic CSV file.')
        return self.engine.create(path)

    def list_jobs(self):
        with sqlite3.connect(self.engine.db_path) as db:
            identifiers = [row[0] for row in db.execute('SELECT id FROM jobs ORDER BY created,id')]
        return [self.engine.inspect(identifier) for identifier in identifiers]

    def inspect(self, identifier):
        return self.engine.inspect(identifier)

    def run(self, identifier, progress):
        return self.engine.run(identifier, progress)

    def cancel(self, identifier):
        self.engine.cancel(identifier)

    def review(self, identifier):
        self.engine.verify(identifier)  # Recheck actual bytes before displaying evidence.
        return self.engine.inspect(identifier)


class Presentation:
    """Single active run, bounded latest progress; thread completion is explicit."""
    def __init__(self, service):
        self.service = service
        self.selected = None
        self.thread = None
        self.lock = threading.Lock()
        self.progress = None
        self.error = None

    def select_input(self, path, operation='exact_duplicates'):
        if self.thread and self.thread.is_alive():
            raise JobError('UI_BUSY', 'Cancel or wait for the active job before creating another.')
        if operation != 'exact_duplicates':
            raise JobError('UI_CONFIGURATION', 'Only exact duplicate removal is supported.')
        job = self.service.create(path)
        self.selected = job['id']
        with self.lock:
            self.error = self.progress = None
        return job

    def _selected(self):
        if not self.selected:
            raise JobError('UI_SELECTION', 'Select a CSV input first.')
        return self.selected

    def start(self):
        identifier = self._selected()
        if self.thread and self.thread.is_alive():
            raise JobError('UI_BUSY', 'A job is already running.')
        with self.lock:
            self.error = self.progress = None
        def update(event):
            with self.lock:
                self.progress = dict(event)
        def work():
            try:
                self.service.run(identifier, update)
            except JobError as exc:
                with self.lock:
                    self.error = exc.as_dict()
            except (OSError, sqlite3.Error):
                with self.lock:
                    self.error = JobError('STORAGE_ERROR', 'Local storage failed; inspect and recover the job.', retryable=True).as_dict()
            except Exception:
                with self.lock:
                    self.error = JobError('UI_INTERNAL', 'Execution interrupted unexpectedly; inspect and recover the job.').as_dict()
        self.thread = threading.Thread(target=work, name='p5-local-job', daemon=False)
        self.thread.start()

    def cancel(self):
        self.service.cancel(self._selected())

    def wait(self, timeout=35):
        if self.thread:
            self.thread.join(timeout)
            if self.thread.is_alive():
                raise JobError('UI_WAIT_TIMEOUT', 'Job is still active; cancel or wait again.', retryable=True)
        return self.status()

    def status(self):
        job = self.service.inspect(self._selected())
        with self.lock:
            return {'job': job, 'progress': self.progress, 'error': self.error,
                    'active': bool(self.thread and self.thread.is_alive()),
                    'delivery_notice': 'Human review required. No approval or export is provided.'}

    def review(self):
        if self.thread and self.thread.is_alive():
            raise JobError('UI_BUSY', 'Wait for processing before reviewing outputs.')
        return self.service.review(self._selected())


def main(argv=None):
    parser = argparse.ArgumentParser(description='P5 local terminal workflow, not a native desktop GUI')
    parser.add_argument('--workspace', required=True)
    parser.add_argument('--demo', help='Process one synthetic CSV and show real review/checksum evidence')
    args = parser.parse_args(argv)
    ui = Presentation(JobService(args.workspace))
    def display(value):
        print(json.dumps(value, ensure_ascii=True, sort_keys=True), flush=True)
    try:
        if args.demo:
            ui.select_input(args.demo)
            ui.start()
            result = ui.wait()
            display(result)
            if result['error'] or result['job']['state'] != 'REVIEW_REQUIRED':
                return 1
            display(ui.review())
            return 0
        print('Freelance Automation Studio — P5 local interface\nCommands: list | select "file.csv" | start | cancel | status | review | wait | quit\nConfiguration: exact_duplicates; original preserved; outputs require human review.')
        while True:
            try:
                tokens = shlex.split(input('FAS> '), posix=False)
                if not tokens:
                    continue
                action = tokens[0]
                if action == 'quit':
                    if ui.thread and ui.thread.is_alive():
                        ui.cancel()
                        ui.wait()
                    return 0
                if action == 'select' and len(tokens) == 2:
                    display(ui.select_input(tokens[1].strip('"')))
                elif len(tokens) == 1 and action in {'list','start','cancel','status','review','wait'}:
                    if action == 'list':
                        display(ui.service.list_jobs())
                    else:
                        display(getattr(ui, action)())
                else:
                    display({'error': {'code': 'UI_COMMAND', 'message': 'Use one of the listed commands; quote paths containing spaces.'}})
            except JobError as exc:
                display({'error': exc.as_dict()})
            except ValueError:
                display({'error': {'code': 'UI_COMMAND', 'message': 'Check command quoting.'}})
            except (EOFError, KeyboardInterrupt):
                if ui.thread and ui.thread.is_alive():
                    ui.cancel()
                    ui.wait()
                return 0
    except JobError as exc:
        display({'error': exc.as_dict()})
        return 1
    except (OSError, sqlite3.Error):
        display({'error': {'code': 'STORAGE_ERROR', 'message': 'Local storage failed.'}})
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
