from PyQt6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QVBoxLayout, QWidget, QTextEdit, QToolBar

from PyQt6.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.toolbar = QToolBar("Toolbar")
        self.toolbar.setMovable(False)
        MainWindow.addToolBar(self.toolbar)

        self.credentials_layout = QHBoxLayout()
        self.credentials_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.userlist_label = QLabel('User:')
        self.credentials_layout.addWidget(self.userlist_label)
        self.userlist_combo = QComboBox()
        self.userlist_combo.setFixedWidth(210)
        self.credentials_layout.addWidget(self.userlist_combo)
        self.refresh_button = QPushButton('↻')
        self.refresh_button.setFixedWidth(30)
        self.refresh_button.setToolTip('Refresh user list')
        self.credentials_layout.addWidget(self.refresh_button)
        self.validity_label = QLabel('Choose a user')
        self.credentials_layout.addWidget(self.validity_label)

        self.users_layout = QVBoxLayout()
        self.users_layout.addLayout(self.credentials_layout)

        self.trial_layout = QVBoxLayout()
        self.add_user_hint = QLabel('To add a new user, click the "Add" button in the settings')
        self.add_user_hint.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.trial_layout.addWidget(self.add_user_hint)

        self.trial_label = QLabel('You can obtain a trial key by following the link: https://aviso.xserv.pp.ua/')
        self.trial_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.trial_layout.addWidget(self.trial_label)

        self.browser_layout = QHBoxLayout()
        self.browser_label = QLabel('Browser:')
        self.browser_layout.addWidget(self.browser_label)
        self.web_browser_combo = QComboBox()
        self.web_browser_combo.addItem('Chrome')
        self.web_browser_combo.addItem('Firefox')
        self.browser_layout.addWidget(self.web_browser_combo)

        self.button_layout = QHBoxLayout()
        self.start_bot_button = QPushButton('Run')
        self.start_bot_button.setEnabled(False)
        self.button_layout.addWidget(self.start_bot_button)
        self.stop_bot_button = QPushButton('Stop')
        self.button_layout.addWidget(self.stop_bot_button)
        self.stop_bot_button.setEnabled(False)
        self.status_label = QLabel('Status: Stopped')
        self.button_layout.addWidget(self.status_label)

        self.money_layout = QHBoxLayout()
        self.earned_money = QLabel('Earned money:')
        self.money_layout.addWidget(self.earned_money)
        self.earned_money_label = QLabel('0.00')
        self.money_layout.addWidget(self.earned_money_label)
        self.money_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        
        self.layout = QVBoxLayout()
        #self.layout.addWidget(self.toolbar)
        self.layout.addLayout(self.users_layout)
        self.layout.addLayout(self.trial_layout)
        self.layout.addLayout(self.browser_layout)
        self.layout.addWidget(self.log_box)
        self.layout.addLayout(self.button_layout)
        self.layout.addLayout(self.money_layout)

        self.centralwidget.setLayout(self.layout)
        MainWindow.setCentralWidget(self.centralwidget)
