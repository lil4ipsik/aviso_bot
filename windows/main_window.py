# This Python file uses the following encoding: utf-8
from os import getenv
from os.path import exists, join, dirname
from threading import Event

from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QMessageBox
from dotenv import load_dotenv

from bot import Bot
from business import is_key_valid, logtime
from ui.main_ui import Ui_MainWindow as MainUI
from version import version as app_version


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.selected_browser = None
        icon_path = join(dirname(__file__), 'icon.ico')
        self.setWindowIcon(QIcon(icon_path))
        self.version = app_version()
        self.setWindowTitle(f'aviso.bz bot ({self.version} - Not activated)')
        self.ui = MainUI()
        self.key_data = (False, None)
        self.ui.setupUi(self)
        self.on_setup_ui()
        self.bot_state = 'stop'
        self.exit_event = Event()
        self.bot = Bot(self.exit_event,
                       self.ui,
                       self.ui.login_edit.text(),
                       self.ui.password_edit.text()
                       )
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ui_update)
        self.ui.start_bot_button.clicked.connect(self.start_bot_button_clicked)
        self.ui.stop_bot_button.clicked.connect(self.stop_bot_button_clicked)
        self.show()
        bar = self.ui.log_box.verticalScrollBar()
        bar.rangeChanged.connect(lambda: bar.setValue(bar.maximum()))
        self.ui.product_key_edit.textChanged.connect(self.check_key)
        self.ui.login_edit.textChanged.connect(self.check_key)

    def check_key(self):
        if len(self.ui.product_key_edit.text()) < 29:
            self.ui.vaild_label.setText('Not enough symbols')
            self.setWindowTitle(f'aviso.bz bot ({self.version} - Not activated)')

        if len(self.ui.product_key_edit.text()) == 29:
            self.key_data = is_key_valid(self.ui.login_edit.text(), self.ui.product_key_edit.text())
            if self.key_data[0]:
                self.ui.vaild_label.setText(f'Valid to {self.key_data[1]}')
                self.setWindowTitle(f'aviso.bz bot ({self.version} - Premium)')
            else:
                self.ui.vaild_label.setText('Invalid (idi nahui)')
                self.setWindowTitle(f'aviso.bz bot ({self.version} - Not activated)')

    def start_bot_button_clicked(self):

        if not self.ui.login_edit.text() or not self.ui.product_key_edit.text() or not self.ui.password_edit.text():
            QMessageBox.warning(self, 'Error', 'Please fill in all fields.')
            return

        if not self.key_data[0]:
            QMessageBox.warning(self, 'Error', 'Invalid key.')
            return

        if self.bot_state == 'stop':
            self.bot_state = 'running'
            self.exit_event.clear()
            self.timer.start(1000)
            self.ui.start_bot_button.setText('Pause')
            self.ui.login_edit.setDisabled(True)
            self.ui.product_key_edit.setDisabled(True)
            self.ui.password_edit.setDisabled(True)
            self.ui.comboBox.setDisabled(True)
            self.ui.web_site_combo.setDisabled(True)
            self.ui.stop_bot_button.setEnabled(True)
            self.ui.status_label.setText('Status: Running')
            self.selected_browser = self.ui.comboBox.currentText()
            self.bot.start()
            # self.bot_thread.daemon = True
            # self.bot_thread.start()
        elif self.bot_state == 'running':
            self.bot_state = 'pause'
            self.ui.status_label.setText('Status: Paused')
            self.exit_event.set()
            self.ui.start_bot_button.setText('Resume')
        elif self.bot_state == 'pause':
            self.bot_state = 'running'
            self.ui.status_label.setText('Status: Running')
            self.exit_event.clear()
            self.ui.start_bot_button.setText('Pause')

    def stop_bot_button_clicked(self):
        self.timer.stop()
        if not self.bot.driver:
            return
        self.ui.log_box.append(f'{logtime()} Please, wait for the bot stop message')
        self.bot.stop()
        self.bot.terminate()
        self.bot.wait()
        self.ui.start_bot_button.setText('Run')
        self.ui.start_bot_button.setDisabled(False)
        self.ui.stop_bot_button.setDisabled(True)
        self.ui.login_edit.setDisabled(False)
        self.ui.product_key_edit.setDisabled(False)
        self.ui.password_edit.setDisabled(False)
        self.ui.comboBox.setDisabled(False)
        self.bot_state = 'stop'
        self.ui.status_label.setText('Status: Stopped')

    def ui_update(self):
        self.ui.earned_money_label.setText(f'{round(self.bot.get_balance(), 5)}')
        if self.bot.is_running:
            self.ui.start_bot_button.setDisabled(False)
            self.ui.stop_bot_button.setDisabled(False)

    def on_setup_ui(self):
        if exists('.env'):
            load_dotenv('.env')
            self.ui.login_edit.setText(getenv('login'))
            self.ui.product_key_edit.setText(getenv('key'))
            self.ui.password_edit.setText(getenv('password'))
            self.check_key()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit', 'Are you sure you want to exit?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
            self.exit_event.set()
            if self.bot.driver is not None:
                self.ui.log_box.append(f'{logtime()} Closing selenium processes...')
                self.bot.driver.quit()
        else:
            event.ignore()
