# This Python file uses the following encoding: utf-8
import os.path
import threading
from datetime import datetime

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow
from dotenv import load_dotenv

from business import Bot
from ui.main_ui import Ui_MainWindow as MainUI


load_dotenv()
# Important:
# You need to run the following command to generate the login_ui.py file
#     pyside6-uic main.ui -o login_ui.py, or
#     pyside2-uic main.ui -o login_ui.py


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.bot_thread = None
        self.ui = MainUI()
        self.ui.setupUi(self)
        self.on_setup_ui()
        self.bot_state = 'stop'
        self.exit_event = threading.Event()
        self.bot = Bot(self.exit_event, self.ui)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ui_update)
        self.timer.start(1000)
        self.ui.start_bot_button.clicked.connect(self.start_bot_button_clicked)
        self.show()

    def start_bot_button_clicked(self):
        if self.bot_state == 'stop':
            self.bot_state = 'running'
            self.exit_event.clear()
            self.ui.start_bot_button.setText('Pause')
            self.bot_thread = threading.Thread(target=self.bot.run_bot, args=(self.ui.login_edit.text(),
                                                                              self.ui.password_edit.text()))
            self.bot_thread.start()
        elif self.bot_state == 'running':
            self.bot_state = 'pause'
            self.exit_event.set()
            self.ui.start_bot_button.setText('Resume')
        elif self.bot_state == 'pause':
            self.bot_state = 'running'
            self.exit_event.clear()
            self.ui.start_bot_button.setText('Pause')

    def ui_update(self):
        self.ui.earned_money_label.setText(f'{self.bot.get_balance()}')

    def on_setup_ui(self):
        if os.path.exists('.env'):
            self.ui.login_edit.setText(os.getenv('login'))
            self.ui.password_edit.setText(os.getenv('password'))
