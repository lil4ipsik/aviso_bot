from datetime import datetime
from os import getenv
from os.path import exists, join, dirname
from threading import Event, Thread

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QIcon
from dotenv import load_dotenv

from business import KeyValidationThread
from bot import Bot
from ui.main_ui import Ui_MainWindow as MainUI
from version import version as app_version
import json
from userdata import create_user_data_file, get_user_data

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        icon_path = join(dirname(__file__), 'icon.ico')
        self.setWindowIcon(QIcon(icon_path))
        self.setFixedSize(410, 300)
        self.version = app_version()
        self.setWindowTitle(f'aviso.bz bot ({self.version} - Not activated)')
        self.bot_thread = None
        self.ui = MainUI()
        self.key_data = (False, None)
        self.ui.setupUi(self)
        #self.on_setup_ui()
        self.ui.toolbar.addAction('Settings', self.open_settings_window)
        self.ui.refresh_button.clicked.connect(self.load_user_data)
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
        self.load_user_data()
        self.ui.userlist_combo.currentIndexChanged.connect(self.check_key)
       #self.ui.product_key_edit.textChanged.connect(self.check_key)
       #self.ui.login_edit.textChanged.connect(self.check_key)

    def check_key(self):
        id = self.ui.userlist_combo.currentIndex() + 1
        user_data = get_user_data()
        
        self.username = user_data.get(str(id), {}).get('username')
        self.key = user_data.get(str(id), {}).get('key')
        self.current_site = user_data.get(str(id), {}).get('site')
        self.password = user_data.get(str(id), {}).get('password')
        if not self.username or not self.key:
            return

        self.key_thread = KeyValidationThread(username=self.username, key=self.key)
        self.key_thread.key_validation_signal.connect(self.key_validation_signal)
        self.key_thread.finished.connect(self.key_thread.deleteLater)
        self.key_thread.start()

    def key_validation_signal(self, is_valid, valid_to):
        if is_valid:
            self.ui.validity_label.setText(f'Valid to: {valid_to}')
            self.setWindowTitle(f'aviso.bz bot ({self.version} - Premium)')
            self.ui.start_bot_button.setEnabled(True)
        else:
            self.ui.validity_label.setText('Invalid (idi nahui)')
            self.setWindowTitle(f'aviso.bz bot ({self.version} - Not activated)')
            self.ui.start_bot_button.setDisabled(True)
        self.key_data = is_valid, valid_to

    def start_bot_button_clicked(self):

        if self.bot_state == 'stop':
            self.bot_state = 'running'
            self.exit_event.clear()
            self.timer.start(1000)
            self.ui.start_bot_button.setText('Pause')
            self.ui.userlist_combo.setDisabled(True)
            self.ui.web_site_combo.setDisabled(True)
            self.ui.stop_bot_button.setEnabled(True)
            self.ui.status_label.setText('Status: Running')
            self.selected_browser = self.ui.web_site_combo.currentText()
            self.bot_thread = Thread(target=self.bot.run_bot, args=(self.username,
                                                                    self.password,
                                                                    self.selected_browser,
                                                                    self.current_site))
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
        self.ui.userlist_combo.setDisabled(False)
        self.ui.web_site_combo.setDisabled(False)
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

    def logtime(self):
        return f'[{datetime.now().replace(microsecond=0)}]'

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit', 'Are you sure you want to exit?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.exit_event.set()
            if self.bot.driver is not None:
                self.ui.log_box.append(f'{self.logtime()} Closing selenium processes...')
                self.bot.driver.quit()
            event.accept()
        else:
            event.ignore()

    def load_user_data(self):
        self.ui.userlist_combo.clear()
        user_data = get_user_data()
        for user_id, user_info in user_data.items():
            self.ui.userlist_combo.addItem(f'{user_id}. {user_info['username']} ({user_info['site']})')


    def open_settings_window(self):
        from windows.settings_window import SettingsWindow
        settings_window = SettingsWindow()
        settings_window.show()