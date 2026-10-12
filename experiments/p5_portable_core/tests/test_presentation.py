"""Real-engine presentation integration tests with synthetic temporary inputs."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest

from experiments.p5_portable_core.core import JobError, checksum
from experiments.p5_portable_core.presentation import JobService, Presentation


class PresentationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / 'synthetic.csv'
        self.source.write_text('id,name\n1,A\n1,A\n2,B\n')
        self.original = checksum(self.source)
        self.ui = Presentation(JobService(self.root / 'workspace'))

    def run_job(self):
        job = self.ui.select_input(self.source)
        self.ui.start()
        self.ui.wait()
        return job

    def test_creation_and_persisted_dashboard(self):
        job = self.ui.select_input(self.source)
        self.assertEqual(self.ui.service.list_jobs()[0]['id'], job['id'])
        self.assertEqual(JobService(self.root/'workspace').list_jobs()[0]['id'], job['id'])

    def test_invalid_input_and_configuration(self):
        for path, op in [(self.root/'missing.csv','exact_duplicates'), (self.root/'file.pdf','exact_duplicates'), (self.source,'fuzzy')]:
            with self.subTest(path=path), self.assertRaises(JobError):
                self.ui.select_input(path, op)
        self.assertEqual(self.ui.service.list_jobs(), [])

    def test_missing_selection(self):
        with self.assertRaises(JobError):
            self.ui.start()

    def test_progress_status_and_review_checksums(self):
        self.run_job()
        status = self.ui.status()
        self.assertEqual(status['job']['state'], 'REVIEW_REQUIRED')
        self.assertEqual(status['progress']['input_rows'], 3)
        self.assertFalse(status['active'])
        artifact = self.ui.review()['artifacts'][-1]
        output = self.root/'workspace'/artifact['path']
        self.assertEqual(checksum(output), artifact['sha256'])
        self.assertEqual(output.read_text(), 'id,name\n1,A\n2,B\n')

    def test_original_and_approval_preserved(self):
        self.run_job()
        self.assertEqual(checksum(self.source), self.original)
        result = self.ui.review()
        self.assertFalse(result['delivery_approved'])
        self.assertEqual(result['attempts'][-1]['review'], 'PENDING')

    def test_processing_failure(self):
        self.source.write_text('id,name\n1\n')
        self.run_job()
        status = self.ui.status()
        self.assertEqual(status['job']['state'], 'FAILED')
        self.assertEqual(status['error']['code'], 'INPUT_SCHEMA')
        self.assertFalse(status['job']['delivery_approved'])

    def test_cancellation_and_busy_controls(self):
        entered, release = threading.Event(), threading.Event()
        def hook(name, context):
            if name == 'row_written':
                entered.set()
                if not release.wait(5):
                    raise RuntimeError('Test synchronization timed out')
        self.ui = Presentation(JobService(self.root/'workspace', fault_hook=hook))
        self.ui.select_input(self.source)
        self.ui.start()
        try:
            self.assertTrue(entered.wait(5))
            with self.assertRaises(JobError): self.ui.start()
            with self.assertRaises(JobError): self.ui.select_input(self.source)
            with self.assertRaises(JobError): self.ui.review()
            self.ui.cancel()
        finally:
            release.set()
            self.ui.wait()
        self.assertEqual(self.ui.status()['job']['state'], 'CANCELLED')
        self.assertEqual(checksum(self.source), self.original)

    def test_tampered_artifact_review_rejected(self):
        self.run_job()
        artifact = self.ui.status()['job']['artifacts'][-1]
        (self.root/'workspace'/artifact['path']).write_text('tampered')
        with self.assertRaises(JobError): self.ui.review()
        self.assertFalse(self.ui.status()['job']['delivery_approved'])

    def test_runnable_demo(self):
        run = subprocess.run([sys.executable,'-m','experiments.p5_portable_core.presentation','--workspace',str(self.root/'demo'),'--demo',str(self.source)],capture_output=True,text=True,timeout=10)
        self.assertEqual(run.returncode,0,run.stderr)
        records = [json.loads(line) for line in run.stdout.splitlines()]
        self.assertEqual(records[0]['job']['state'],'REVIEW_REQUIRED')
        self.assertFalse(records[-1]['delivery_approved'])

    def test_interactive_workflow(self):
        commands = f'select "{self.source}"\nstart\nwait\nreview\nlist\nquit\n'
        run = subprocess.run([sys.executable,'-m','experiments.p5_portable_core.presentation','--workspace',str(self.root/'interactive')],input=commands,capture_output=True,text=True,timeout=10)
        self.assertEqual(run.returncode,0,run.stderr)
        self.assertIn('REVIEW_REQUIRED',run.stdout)
        self.assertIn('sha256',run.stdout)
        self.assertNotIn('UI_INTERNAL',run.stdout)


if __name__ == '__main__':
    unittest.main()
