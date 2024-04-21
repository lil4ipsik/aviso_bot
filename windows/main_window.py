# This Python file uses the following encoding: utf-8
from datetime import datetime
from os import getenv
from os.path import exists, join, dirname
from threading import Event, Thread

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
from dotenv import load_dotenv

from business import Bot, is_key_valid, get_date_expire_from_code
from ui.main_ui import Ui_MainWindow as MainUI
from PySide6.QtWidgets import QMessageBox
from version import version as app_version

# Important:
# You need to run the following command to generate the login_ui.py file
#     pyside6-uic ./res/ui/main.ui -o ./ui/main_ui.py.


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        icon_path = join(dirname(__file__), 'icon.ico')
        self.setWindowIcon(QIcon(icon_path))
        self.version = app_version()
        self.setWindowTitle(f'aviso.bz bot ({self.version} - Not activated)')
        self.bot_thread = None
        self.ui = MainUI()
        self.ui.setupUi(self)
        self.on_setup_ui()
        self.bot_state = 'stop'
        self.exit_event = Event()
        self.bot = Bot(self.exit_event, self.ui)
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
            if is_key_valid(self.ui.login_edit.text(), self.ui.product_key_edit.text()):
                valid_date = get_date_expire_from_code(self.ui.product_key_edit.text())
                self.ui.vaild_label.setText(f'Valid until {valid_date["year"]}-{valid_date["month"]}-{valid_date["day"]}')
                self.setWindowTitle(f'aviso.bz bot ({self.version} - Premium)')
            else:
                self.ui.vaild_label.setText('Invalid (idi nahui)')
                self.setWindowTitle(f'aviso.bz bot ({self.version} - Not activated)')

    def start_bot_button_clicked(self):
        if not self.is_valid_product_key():
            self.stop_bot_button_clicked()
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
            self.ui.status_label.setText('Status: Running')
            self.selected_browser = self.ui.comboBox.currentText()
            self.bot_thread = Thread(target=self.bot.run_bot, args=(self.ui.login_edit.text(),
                                                                    self.ui.password_edit.text(),
                                                                    self.selected_browser))
            self.bot_thread.daemon = True
            self.bot_thread.start()
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
        self.ui.start_bot_button.setText('Run')
        self.ui.start_bot_button.setDisabled(False)
        self.ui.stop_bot_button.setDisabled(True)
        self.ui.login_edit.setDisabled(False)
        self.ui.product_key_edit.setDisabled(False)
        self.ui.password_edit.setDisabled(False)
        self.ui.comboBox.setDisabled(False)
        self.bot_state = 'stop'
        self.ui.status_label.setText('Status: Stopped')
        Thread(target=self.bot.stop).start()

    def ui_update(self):
        self.ui.earned_money_label.setText(f'{round(self.bot.get_balance(), 5)}')
        if self.bot.is_running:
            self.ui.start_bot_button.setDisabled(False)
            self.ui.stop_bot_button.setDisabled(False)

    def on_setup_ui(self):
        if exists('.env'):
            load_dotenv('.env')
            # print('File exists')
            self.ui.login_edit.setText(getenv('login'))
            self.ui.product_key_edit.setText(getenv('key'))
            self.ui.password_edit.setText(getenv('password'))
            self.check_key()

    def is_valid_product_key(self):
        if is_key_valid(self.ui.login_edit.text(), self.ui.product_key_edit.text()):
            return True
        else:
            self.ui.log_box.setText(f'<font color="green">{self.logtime()} Product key invalid</font>')
            return False

    def logtime(self):
        return f'[{datetime.now().replace(microsecond=0)}]'

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit', 'Are you sure you want to exit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            self.exit_event.set()
            if self.bot.driver is not None:
                self.ui.log_box.append(f'{self.logtime()} Closing selenium processes...')
                self.bot.driver.quit()
        else:
            event.ignore()
