# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QVBoxLayout, QWidget, QTextEdit

from PyQt6.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.setFixedSize(410, 400)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.credentials_layout = QHBoxLayout()
        self.login_label = QLabel('Login:')
        self.credentials_layout.addWidget(self.login_label)
        self.login_edit = QLineEdit()
        self.credentials_layout.addWidget(self.login_edit)
        self.password_label = QLabel('Password:')
        self.credentials_layout.addWidget(self.password_label)
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.credentials_layout.addWidget(self.password_edit)

        self.key_layout = QHBoxLayout()
        self.product_key_label = QLabel('Product key:')
        self.key_layout.addWidget(self.product_key_label)
        self.product_key_edit = QLineEdit()
        self.key_layout.addWidget(self.product_key_edit)
        self.vaild_label = QLabel('Not activated')
        self.key_layout.addWidget(self.vaild_label)

        self.trial_layout = QVBoxLayout()
        self.trial_layout.addLayout(self.key_layout)
        self.trial_label = QLabel('You can obtain a trial key by following the link: https://aviso.xserv.pp.ua/')
        self.trial_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.trial_layout.addWidget(self.trial_label)

        self.browser_layout = QHBoxLayout()
        self.browser_label = QLabel('Browser:')
        self.browser_layout.addWidget(self.browser_label)
        self.comboBox = QComboBox()
        self.comboBox.addItem('Chrome')
        self.comboBox.addItem('Firefox')
        self.browser_layout.addWidget(self.comboBox)

        self.button_layout = QHBoxLayout()
        self.start_bot_button = QPushButton('Run')
        self.button_layout.addWidget(self.start_bot_button)
        self.stop_bot_button = QPushButton('Stop')
        self.button_layout.addWidget(self.stop_bot_button)
        self.status_label = QLabel('Status: Stopped')
        self.button_layout.addWidget(self.status_label)

        self.money_layout = QHBoxLayout()
        self.earned_money = QLabel('Earned money:')
        self.money_layout.addWidget(self.earned_money)
        self.earned_money_label = QLabel('0.00')
        self.money_layout.addWidget(self.earned_money_label)
        self.money_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.site_layout = QHBoxLayout()
        self.site_label = QLabel('Site:')
        self.site_layout.addWidget(self.site_label)
        self.web_site_combo = QComboBox()
        self.web_site_combo.addItem('Aviso')
        self.web_site_combo.addItem('Proficentr')
        self.site_layout.addWidget(self.web_site_combo)

        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.credentials_layout)
        self.layout.addLayout(self.trial_layout)
        self.layout.addLayout(self.browser_layout)
        self.layout.addLayout(self.site_layout)
        self.layout.addWidget(self.log_box)
        self.layout.addLayout(self.button_layout)
        self.layout.addLayout(self.money_layout)

        self.centralwidget.setLayout(self.layout)
        MainWindow.setCentralWidget(self.centralwidget)
