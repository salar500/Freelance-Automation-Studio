"""P5 Qt widget experiment; the processing core has no Qt dependency."""
import argparse
from pathlib import Path

from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                              QHBoxLayout, QLabel, QPushButton, QLineEdit,
                              QFileDialog, QComboBox, QListWidget, QPlainTextEdit)
from .core import JobError
from .presentation import JobService, Presentation


class Window(QMainWindow):
    def __init__(self, workspace=None, *, presentation=None):
        super().__init__()
        self.ui = presentation or Presentation(JobService(workspace))
        self.setWindowTitle('Freelance Automation Studio — P5 experiment')
        self.resize(960, 680)
        self.closing = False
        self.setCentralWidget(QWidget())
        layout = QVBoxLayout(self.centralWidget())
        heading = QLabel('Freelance Automation Studio')
        heading.setStyleSheet('font-size:24px;font-weight:600')
        layout.addWidget(heading)
        layout.addWidget(QLabel('Local CSV jobs • Synthetic data only • Human review required'))
        row = QHBoxLayout()
        self.path = QLineEdit()
        self.path.setAccessibleName('CSV input path')
        self.path.setPlaceholderText('Select a synthetic CSV file')
        self.browse = QPushButton('Browse CSV…')
        self.create = QPushButton('Create job')
        row.addWidget(self.path, 1); row.addWidget(self.browse); row.addWidget(self.create)
        layout.addLayout(row)
        self.operation = QComboBox()
        self.operation.addItem('Remove exact duplicate rows (preserve first occurrence)', 'exact_duplicates')
        self.operation.setAccessibleName('Job operation')
        layout.addWidget(self.operation)
        self.jobs = QListWidget()
        self.jobs.setAccessibleName('Persisted jobs')
        layout.addWidget(self.jobs)
        actions = QHBoxLayout()
        self.start = QPushButton('Start')
        self.cancel = QPushButton('Cancel processing')
        self.review = QPushButton('Review output integrity')
        self.refresh = QPushButton('Refresh jobs')
        for button in [self.start,self.cancel,self.review,self.refresh]: actions.addWidget(button)
        layout.addLayout(actions)
        self.status = QLabel('No job selected')
        self.progress = QLabel('No progress yet')
        self.feedback = QLabel('')
        self.feedback.setWordWrap(True)
        layout.addWidget(self.status);layout.addWidget(self.progress);layout.addWidget(self.feedback)
        self.details = QPlainTextEdit()
        self.details.setReadOnly(True)
        self.details.setAccessibleName('Output and checksum details')
        layout.addWidget(self.details, 1)
        layout.addWidget(QLabel('Processing success does not approve delivery. Approval and export are unavailable.'))
        self.browse.clicked.connect(self.choose_file)
        self.create.clicked.connect(self.create_job)
        self.start.clicked.connect(lambda: self.invoke(self.ui.start))
        self.cancel.clicked.connect(lambda: self.invoke(self.ui.cancel))
        self.review.clicked.connect(self.review_output)
        self.refresh.clicked.connect(self.refresh_jobs)
        self.jobs.currentRowChanged.connect(self.select_job)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick)
        self.timer.start(75)
        self.refresh_jobs()
        self.tick()

    def error(self, exc):
        self.feedback.setText(f'{exc.code}: {exc.message} Affected: current job/input. Next: correct input or inspect/recover the job.')

    def invoke(self, action):
        try:
            action()
            self.feedback.clear()
        except JobError as exc:
            self.error(exc)
        except Exception:
            self.error(JobError('UI_STORAGE', 'Local action failed; no success is assumed.'))
        self.tick()

    def choose_file(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Select synthetic CSV', '', 'CSV files (*.csv)')
        if name:
            self.path.setText(name)

    def create_job(self):
        def create():
            self.ui.select_input(self.path.text(), self.operation.currentData())
            self.refresh_jobs()
        self.invoke(create)

    def refresh_jobs(self):
        try:
            jobs = self.ui.service.list_jobs()
            self.jobs.blockSignals(True)
            self.jobs.clear()
            for job in jobs:
                self.jobs.addItem(f"{job['id']} | {job['state']}")
                item = self.jobs.item(self.jobs.count()-1)
                item.setData(Qt.ItemDataRole.UserRole, job['id'])
                if job['id'] == self.ui.selected:
                    self.jobs.setCurrentItem(item)
            self.jobs.blockSignals(False)
        except Exception:
            self.jobs.blockSignals(False)
            self.error(JobError('UI_STORAGE', 'Job history could not be loaded.'))

    def select_job(self, row):
        if self.ui.thread and self.ui.thread.is_alive():
            return
        item = self.jobs.item(row)
        if item:
            self.ui.selected = item.data(Qt.ItemDataRole.UserRole)
            with self.ui.lock:
                self.ui.progress = self.ui.error = None
            self.feedback.clear()
            self.tick()

    def review_output(self):
        self.invoke(self.ui.review)

    def tick(self):
        active = bool(self.ui.thread and self.ui.thread.is_alive())
        for widget in [self.path,self.browse,self.create,self.operation,self.jobs]:
            widget.setEnabled(not active and not self.closing)
        self.cancel.setEnabled(active and not self.closing)
        self.start.setEnabled(False)
        self.review.setEnabled(False)
        if not self.ui.selected:
            return
        try:
            result = self.ui.status()
            job = result['job']
            self.status.setText(f"Job: {job['state']} | Delivery approval: NOT APPROVED")
            self.start.setEnabled(not active and not self.closing and job['state'] in {'READY','FAILED','CANCELLED','INTERRUPTED'})
            self.review.setEnabled(not active and not self.closing and job['state']=='REVIEW_REQUIRED')
            if result['progress']:
                p = result['progress']
                self.progress.setText(f"Last observed progress: {p['input_rows']} rows read, {p['output_rows']} kept, {p['duplicates']} duplicates")
            else:
                self.progress.setText('No row progress recorded for this view')
            error = result['error'] or job['error']
            if error:
                self.error(JobError(error['code'],error['message']))
            lines = [f"Input SHA-256: {job['input_sha256']}"]
            for attempt in job['attempts']:
                lines.append(f"Rows: {attempt['input_rows']} → {attempt['output_rows']} | Validation: {attempt['validation']} | Review: {attempt['review']}")
            for artifact in job['artifacts']:
                lines.extend([f"Output: {artifact['path']}",f"Bytes: {artifact['bytes']} | Integrity: {artifact['status']}",f"SHA-256: {artifact['sha256']}"])
            self.details.setPlainText('\n'.join(lines))
            if not active:
                for index in range(self.jobs.count()):
                    item = self.jobs.item(index)
                    if item.data(Qt.ItemDataRole.UserRole)==job['id']:
                        item.setText(f"{job['id']} | {job['state']}")
            if self.closing and not active:
                self.close()
        except Exception:
            self.error(JobError('UI_STORAGE','Status could not be read; processing success is unknown.'))

    def closeEvent(self, event):
        if self.ui.thread and self.ui.thread.is_alive():
            self.closing = True
            self.invoke(self.ui.cancel)
            self.feedback.setText('Cancellation requested. Waiting for processing to stop before closing.')
            event.ignore()
        else:
            self.timer.stop()
            event.accept()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', required=True)
    args = parser.parse_args(argv)
    app = QApplication.instance() or QApplication([])
    try:
        window = Window(args.workspace)
    except Exception:
        parser.exit(1, 'GUI startup failed; check local workspace and GUI dependencies.\n')
    window.show()
    return app.exec()


if __name__ == '__main__':
    raise SystemExit(main())
