"""Actual Qt widget tests. Install the separately pinned experimental GUI extras."""
from pathlib import Path
import tempfile
import threading
import time
import unittest
from unittest.mock import patch

from PySide6.QtCore import Qt, QCoreApplication, QEvent
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication
from experiments.p5_portable_core.gui import Window
from experiments.p5_portable_core.presentation import JobService, Presentation
from experiments.p5_portable_core.core import checksum


class GuiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source = self.root/'synthetic.csv'
        self.source.write_text('id,name\n1,A\n1,A\n2,B\n')
        self.before = checksum(self.source)
        self.window = Window(self.root/'workspace')
        self.window.show()
        self.app.processEvents()

    def tearDown(self):
        if self.window.ui.thread and self.window.ui.thread.is_alive():
            self.window.ui.cancel()
            self.window.ui.wait()
        self.window.close()
        self.window.deleteLater()
        QCoreApplication.sendPostedEvents(None,QEvent.Type.DeferredDelete)
        self.app.processEvents()
        self.temp.cleanup()

    def click(self, button):
        QTest.mouseClick(button,Qt.MouseButton.LeftButton)
        self.app.processEvents()

    def create(self):
        self.window.path.setText(str(self.source))
        self.click(self.window.create)
        self.assertIsNotNone(self.window.ui.selected)

    def finish(self):
        deadline = time.monotonic()+10
        while self.window.ui.thread and self.window.ui.thread.is_alive():
            self.app.processEvents()
            QTest.qWait(5)
            self.assertLess(time.monotonic(),deadline)
        self.window.tick()

    def run_job(self):
        self.create()
        self.click(self.window.start)
        self.finish()

    def test_window_renders_and_file_picker_selects(self):
        self.assertTrue(self.window.isVisible())
        self.assertFalse(self.window.grab().isNull())
        with patch('experiments.p5_portable_core.gui.QFileDialog.getOpenFileName',return_value=(str(self.source),'CSV')):
            self.click(self.window.browse)
        self.assertEqual(self.window.path.text(),str(self.source))
        self.click(self.window.create)
        self.assertEqual(self.window.jobs.count(),1)

    def test_success_real_core_evidence_no_approval(self):
        self.run_job()
        self.assertIn('REVIEW_REQUIRED',self.window.status.text())
        self.assertIn('3 → 2',self.window.details.toPlainText())
        self.assertIn('SHA-256:',self.window.details.toPlainText())
        self.assertIn('3 rows read',self.window.progress.text())
        self.click(self.window.review)
        self.assertFalse(self.window.ui.status()['job']['delivery_approved'])
        self.assertEqual(checksum(self.source),self.before)
        self.assertFalse(self.window.start.isEnabled())

    def test_input_validation(self):
        self.window.path.setText(str(self.root/'missing.csv'))
        self.click(self.window.create)
        self.assertIn('INPUT_MISSING',self.window.feedback.text())
        self.assertEqual(self.window.jobs.count(),0)

    def test_processing_error(self):
        self.source.write_text('id,name\n1\n')
        self.run_job()
        self.assertIn('FAILED',self.window.status.text())
        self.assertIn('INPUT_SCHEMA',self.window.feedback.text())

    def test_tamper_review_invalidates(self):
        self.run_job()
        artifact=self.window.ui.status()['job']['artifacts'][-1]
        (self.root/'workspace'/artifact['path']).write_text('tamper')
        self.click(self.window.review)
        self.assertIn('OUTPUT_INTEGRITY',self.window.feedback.text())
        self.assertIn('REVISION_REQUIRED',self.window.status.text())

    def blocked_window(self):
        self.window.close()
        self.window.deleteLater()
        QCoreApplication.sendPostedEvents(None,QEvent.Type.DeferredDelete)
        entered,release=threading.Event(),threading.Event()
        def hook(name,context):
            if name=='row_written':
                entered.set()
                if not release.wait(5):raise RuntimeError('Synchronization timeout')
        self.window=Window(presentation=Presentation(JobService(self.root/'workspace',fault_hook=hook)))
        self.window.show()
        self.create()
        self.click(self.window.start)
        self.assertTrue(entered.wait(5))
        return release

    def test_cancel_button_and_controls(self):
        release=self.blocked_window()
        try:
            self.window.tick()
            self.assertTrue(self.window.cancel.isEnabled())
            self.assertFalse(self.window.create.isEnabled())
            self.click(self.window.cancel)
        finally:release.set()
        self.finish()
        self.assertIn('CANCELLED',self.window.status.text())
        self.assertEqual(checksum(self.source),self.before)

    def test_close_cancels_then_waits(self):
        release=self.blocked_window()
        try:
            self.window.close()
            self.assertTrue(self.window.isVisible())
            self.assertTrue(self.window.closing)
        finally:release.set()
        self.finish()
        self.assertEqual(self.window.ui.status()['job']['state'],'CANCELLED')
        self.assertFalse(self.window.isVisible())

    def test_history_reload(self):
        self.run_job()
        self.window.close()
        self.window.deleteLater()
        QCoreApplication.sendPostedEvents(None,QEvent.Type.DeferredDelete)
        self.window=Window(self.root/'workspace')
        self.assertEqual(self.window.jobs.count(),1)
        self.window.jobs.setCurrentRow(0)
        self.assertIn('REVIEW_REQUIRED',self.window.status.text())
