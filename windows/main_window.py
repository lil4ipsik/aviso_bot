# This Python file uses the following encoding: utf-8
from os import getenv
from os.path import exists, join, dirname
from threading import Event, Thread

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
from dotenv import load_dotenv

from business import Bot
from ui.main_ui import Ui_MainWindow as MainUI


# Important:
# You need to run the following command to generate the login_ui.py file
#     pyside6-uic ./res/ui/main.ui -o ./ui/main_ui.py.


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        icon_path = join(dirname(__file__), 'icon.ico')
        self.setWindowIcon(QIcon(icon_path))
        self.bot_thread = None
        self.ui = MainUI()
        self.ui.setupUi(self)
        self.on_setup_ui()
        self.bot_state = 'stop'
        self.exit_event = Event()
        self.bot = Bot(self.exit_event, self.ui)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ui_update)
        self.timer.start(1000)
        self.ui.start_bot_button.clicked.connect(self.start_bot_button_clicked)
        self.ui.stop_bot_button.clicked.connect(self.stop_bot_button_clicked)
        self.show()
        bar = self.ui.log_box.verticalScrollBar()
        bar.rangeChanged.connect(lambda: bar.setValue(bar.maximum()))

    def start_bot_button_clicked(self):
        if self.bot_state == 'stop':
            self.bot_state = 'running'
            self.exit_event.clear()
            self.ui.start_bot_button.setText('Pause')
            self.selected_browser = self.ui.comboBox.currentText()
            self.bot_thread = Thread(target=self.bot.run_bot, args=(self.ui.login_edit.text(),
                                                                              self.ui.password_edit.text(), self.selected_browser))
            self.bot_thread.daemon = True
            self.bot_thread.start()
        elif self.bot_state == 'running':
            self.bot_state = 'pause'
            self.exit_event.set()
            self.ui.start_bot_button.setText('Resume')
        elif self.bot_state == 'pause':
            self.bot_state = 'running'
            self.exit_event.clear()
            self.ui.start_bot_button.setText('Pause')

    def stop_bot_button_clicked(self):
        if not self.bot.driver:
            return
        self.ui.start_bot_button.setText('Run')
        self.ui.start_bot_button.setDisabled(True)
        self.ui.stop_bot_button.setDisabled(True)
        self.bot_state = 'stop'
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
            self.ui.password_edit.setText(getenv('password'))

    def closeEvent(self, event):
        self.bot.stop()
        self.timer.stop()
        event.accept()
