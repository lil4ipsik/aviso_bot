import sys
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLineEdit, QComboBox, QMainWindow, QTabWidget , QTreeWidget, QTreeWidgetItem
from PyQt6.QtGui import QIcon
import json
from userdata import add_user, delete_user_by_id, edit_user_by_id
from os import path as p

app_icon_path = p.dirname(p.abspath(__file__)) + '/icon.ico'

class UI_Settings(object):
    def setup_ui(self, SettingsWindow):
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

        self.users_layout = QVBoxLayout()
        self.users_layout.addWidget(self.tree_widget)
        self.users_layout.addLayout(self.buttons_layout)
        self.users_tab.setLayout(self.users_layout)

        self.label2 = QLabel("Content for Tab 2")
        self.layout2 = QVBoxLayout()
        self.layout2.addWidget(self.label2)
        self.about_tab.setLayout(self.layout2)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tab_widget)
        self.centralWidget.setLayout(self.layout)
        SettingsWindow.setCentralWidget(self.centralWidget)
