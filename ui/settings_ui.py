import sys
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QTabWidget , QTreeWidget, QLineEdit
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from os import path as p
from version import version
from webbrowser import open as open_url

class UI_Settings(object):
    def setup_ui(self, SettingsWindow, png_icon_path, github_icon, website_icon):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        
        SettingsWindow.setWindowTitle("Settings")
        SettingsWindow.setFixedSize(600, 400)

        self.centralWidget = QWidget(SettingsWindow)
        self.tab_widget = QTabWidget()

        self.users_tab = QWidget()
        self.about_tab = QWidget()

        self.tab_widget.addTab(self.users_tab, "Users")
        self.tab_widget.addTab(self.about_tab, "About")

        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabels(["ID", "Username", "Password", "Key", "Site"])
        
        self.buttons_layout = QHBoxLayout()
        self.add_button = QPushButton("Add")
        self.buttons_layout.addWidget(self.add_button)
        self.edit_button = QPushButton("Edit")
        self.edit_button.setEnabled(False)
        self.buttons_layout.addWidget(self.edit_button)
        self.remove_button = QPushButton("Remove")
        self.remove_button.setEnabled(False)
        self.buttons_layout.addWidget(self.remove_button)

        self.api_layout = QHBoxLayout()
        self.api_label = QLabel("API Key:")
        self.api_layout.addWidget(self.api_label)
        self.api_edit = QLineEdit()
        self.api_edit.setMaxLength(32)
        self.api_layout.addWidget(self.api_edit)
        self.api_save_button = QPushButton("Save")
        self.api_save_button.setEnabled(False)
        self.api_layout.addWidget(self.api_save_button)

        self.users_layout = QVBoxLayout()
        self.users_layout.addWidget(self.tree_widget)
        self.users_layout.addLayout(self.api_layout)
        self.users_layout.addLayout(self.buttons_layout)
        self.users_tab.setLayout(self.users_layout)

        self.about_buttons_layout = QHBoxLayout()
        self.github_button = QPushButton("Github")
        self.github_button.setIcon(QIcon(github_icon))
        self.github_button.clicked.connect(lambda: open_url("https://github.com/systnager/aviso_bot"))
        self.website_button = QPushButton("Website")
        self.website_button.setIcon(QIcon(website_icon))
        self.website_button.clicked.connect(lambda: open_url("https://aviso.xserv.pp.ua"))
        self.about_buttons_layout.addWidget(self.github_button)
        self.about_buttons_layout.addWidget(self.website_button)

        self.about_layout = QVBoxLayout()
        self.about_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.icon = QLabel()
        self.icon.setPixmap(QPixmap(png_icon_path))
        self.icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.about_layout.addWidget(self.icon)
        self.info = QLabel(f"Aviso bot {version()}\nDeveloped by Lil4ipsik team\n2024")
        self.info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.about_layout.addWidget(self.info)
        self.about_layout.addLayout(self.about_buttons_layout)
        self.about_tab.setLayout(self.about_layout)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tab_widget)
        self.centralWidget.setLayout(self.layout)
        SettingsWindow.setCentralWidget(self.centralWidget)
