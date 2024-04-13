import os
import threading
import time

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QLineEdit, QApplication
from dotenv import load_dotenv

import settings
from ui.login_ui import Ui_MainWindow as LoginUI


load_dotenv()




