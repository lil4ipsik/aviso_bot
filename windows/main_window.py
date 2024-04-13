# This Python file uses the following encoding: utf-8
import logging
import threading
from datetime import datetime

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow

from business import Bot
from ui.main_ui import Ui_MainWindow as MainUI


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
        self.bot_state = 'stop'
        self.exit_event = threading.Event()
        self.bot = Bot(self.exit_event)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ui_update)
        self.timer.start(1000)
        self.ui.start_bot_button.clicked.connect(self.start_bot_button_clicked)

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        handler = QTextEditLogger(self.ui.logs)
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        self.log_message("Початок роботи програми", "green", "white")
        self.show()

    def log_message(self, log_box, message):
        message_with_color = f"<font color='{text_color}'>{message}</font>"
        log_box.append(message_with_color)

    def start_bot_button_clicked(self):
        if self.bot_state == 'stop':
            self.bot_state = 'running'
            self.exit_event.clear()
            self.ui.start_bot_button.setText('Pause')
            self.bot_thread = threading.Thread(target=self.bot.run_bot)
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


class QTextEditLogger(logging.Handler):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        msg = self.format(record)
        self.text_widget.append(msg)
