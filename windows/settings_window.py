import sys
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLineEdit, QComboBox, QDialog, QMainWindow , QTreeWidget, QTreeWidgetItem
from PyQt6.QtGui import QIcon, QPixmap
import json
from userdata import *
from os import path as p
from ui.settings_ui import UI_Settings as SettingsUI

app_icon_path = p.dirname(p.abspath(__file__)) + '/img/icon.ico'
png_icon_path = p.dirname(p.abspath(__file__)) + '/img/icon.png'



class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setFixedSize(600, 400)
        self.setWindowIcon(QIcon(app_icon_path))
        self.ui = SettingsUI()
        self.ui.setup_ui(self, png_icon_path, self.colorscheme()[0], self.colorscheme()[1])
        self.userdata = create_user_data_file()
        self.load_user_data()

        self.ui.add_button.clicked.connect(self.add_user)
        self.ui.edit_button.clicked.connect(lambda: self.edit_user(self.ui.tree_widget.currentItem().text(0), self.ui.tree_widget.currentItem().text(1), self.ui.tree_widget.currentItem().text(2), self.ui.tree_widget.currentItem().text(3), self.ui.tree_widget.currentItem().text(4)))
        self.ui.remove_button.clicked.connect(self.delete_user)

        self.ui.tree_widget.itemClicked.connect(lambda item: [self.ui.edit_button.setEnabled(True), self.ui.remove_button.setEnabled(True)])
        self.ui.tree_widget.itemDoubleClicked.connect(lambda item: [self.edit_user(item.text(0), item.text(1), item.text(2), item.text(3), item.text(4))]) 
        self.ui.tree_widget.itemSelectionChanged.connect(lambda: [self.ui.edit_button.setEnabled(False), self.ui.remove_button.setEnabled(False)])

        self.ui.api_edit.setText(get_api_key())
        self.ui.api_edit.textChanged.connect(lambda: self.ui.api_save_button.setEnabled(bool(len(self.ui.api_edit.text()) == 32 and self.ui.api_edit.text() != get_api_key())))
        self.ui.api_save_button.clicked.connect(self.api_key)

    def load_user_data(self):
        user_data = get_user_data()

        self.ui.tree_widget.clear()
        if user_data:
            for user_id, data in user_data.items():
                item = QTreeWidgetItem([user_id, data['username'], data['password'], data['key'], data['site']])
                self.ui.tree_widget.addTopLevelItem(item)
        else:
            self.ui.tree_widget.clear()

    def add_user(self):
        add_user_window = QDialog(self)
        add_user_window.setWindowTitle("Add user")
        add_user_window.setFixedSize(400, 200)

        username_layout = QHBoxLayout()
        username_label = QLabel("Username:")
        username_edit = QLineEdit()
        username_layout.addWidget(username_label)
        username_layout.addWidget(username_edit)
        password_layout = QHBoxLayout()
        password_label = QLabel("Password:")
        password_edit = QLineEdit()
        password_layout.addWidget(password_label)
        password_layout.addWidget(password_edit)
        key_layout = QHBoxLayout()
        key_label = QLabel("Key:")
        key_edit = QLineEdit()
        key_edit.setPlaceholderText("XXXXX-XXXXX-XXXXX-XXXXX-XXXXX")
        key_edit.setInputMask("XXXXX-XXXXX-XXXXX-XXXXX-XXXXX;X")
        key_edit.setMaxLength(29)
        key_layout.addWidget(key_label)
        key_layout.addWidget(key_edit)
        site_layout = QHBoxLayout()
        site_label = QLabel("Site:")
        site_combo = QComboBox()
        site_combo.addItem("Aviso")
        site_combo.addItem("Profitcentr")
        site_layout.addWidget(site_label)
        site_layout.addWidget(site_combo)

        button_layout = QHBoxLayout()
        save_button = QPushButton("Save")
        button_layout.addWidget(save_button)
        if not username_edit.text() or not password_edit.text() or not key_edit.text():
            save_button.setEnabled(False)
        username_edit.textChanged.connect(lambda: save_button.setEnabled(bool(username_edit.text() and password_edit.text() and key_edit.text())))
        password_edit.textChanged.connect(lambda: save_button.setEnabled(bool(username_edit.text() and password_edit.text() and key_edit.text())))
        key_edit.textChanged.connect(lambda: save_button.setEnabled(bool(username_edit.text() and password_edit.text() and len(key_edit.text()) == 29)))
        save_button.clicked.connect(lambda: [add_user(username_edit.text(), password_edit.text(), key_edit.text(), site_combo.currentText()), self.load_user_data(), add_user_window.close()])  # Close the add_user_window after saving the user data
        cancel_button = QPushButton("Cancel")
        button_layout.addWidget(cancel_button)
        cancel_button.clicked.connect(add_user_window.close)

        layout = QVBoxLayout()
        layout.addLayout(username_layout)
        layout.addLayout(password_layout)
        layout.addLayout(key_layout)
        layout.addLayout(site_layout)
        layout.addLayout(button_layout)

        add_user_window.setLayout(layout)
        add_user_window.show()

    def key_length(self, key):
        return len(key) == 29

    def delete_user(self):
        selected_item = self.ui.tree_widget.currentItem()
        if selected_item is not None:
            user_id = selected_item.text(0)
            print(f"Deleting user with ID {user_id}")
            delete_user_by_id(user_id)
            self.load_user_data()

    def edit_user(self, id, username, password, key, site):
        edit_user_window = QDialog(self)
        edit_user_window.setWindowTitle("Edit user")
        edit_user_window.setFixedSize(400, 200)

        username_layout = QHBoxLayout()
        username_label = QLabel("Username:")
        username_edit = QLineEdit()
        username_edit.setText(username)
        username_layout.addWidget(username_label)
        username_layout.addWidget(username_edit)
        password_layout = QHBoxLayout()
        password_label = QLabel("Password:")
        password_edit = QLineEdit()
        password_edit.setText(password)
        password_layout.addWidget(password_label)
        password_layout.addWidget(password_edit)
        key_layout = QHBoxLayout()
        key_label = QLabel("Key:")
        key_edit = QLineEdit()
        key_edit.setPlaceholderText("XXXXX-XXXXX-XXXXX-XXXXX-XXXXX")
        key_edit.setInputMask("XXXXX-XXXXX-XXXXX-XXXXX-XXXXX;X")
        key_edit.setMaxLength(29)
        key_edit.setText(key)
        key_layout.addWidget(key_label)
        key_layout.addWidget(key_edit)
        site_layout = QHBoxLayout()
        site_label = QLabel("Site:")
        site_combo = QComboBox()
        site_combo.addItem("Aviso")
        site_combo.addItem("Profitcentr")
        site_combo.setCurrentText(site)
        site_layout.addWidget(site_label)
        site_layout.addWidget(site_combo)

        button_layout = QHBoxLayout()
        save_button = QPushButton("Save")
        button_layout.addWidget(save_button)
        if not username_edit.text() or not password_edit.text() or not key_edit.text():
            save_button.setEnabled(False)
        username_edit.textChanged.connect(lambda: save_button.setEnabled(bool(username_edit.text() and password_edit.text() and key_edit.text())))
        password_edit.textChanged.connect(lambda: save_button.setEnabled(bool(username_edit.text() and password_edit.text() and key_edit.text())))
        key_edit.textChanged.connect(lambda: save_button.setEnabled(bool(username_edit.text() and password_edit.text() and len(key_edit.text()) == 29)))
        save_button.clicked.connect(lambda: [edit_user_by_id(id, username_edit.text(), password_edit.text(), key_edit.text(), site_combo.currentText()), self.load_user_data(), edit_user_window.close()])  # Close the add_user_window after saving the user data
        cancel_button = QPushButton("Cancel")
        button_layout.addWidget(cancel_button)
        cancel_button.clicked.connect(edit_user_window.close)

        layout = QVBoxLayout()
        layout.addLayout(username_layout)
        layout.addLayout(password_layout)
        layout.addLayout(key_layout)
        layout.addLayout(site_layout)
        layout.addLayout(button_layout)

        edit_user_window.setLayout(layout)
        edit_user_window.show()

    def api_key(self):
        api_key = self.ui.api_edit.text()
        save_api_key(api_key)

    def colorscheme(self):
        window_color = self.palette().window().color()

        dark_github_icon = QPixmap(p.dirname(p.abspath(__file__)) + '/img/icons/githublogo_dark.png')
        dark_website_icon = QPixmap(p.dirname(p.abspath(__file__)) + '/img/icons/website_dark.png')
        light_github_icon = QPixmap(p.dirname(p.abspath(__file__)) + '/img/icons/githublogo.png')
        light_website_icon = QPixmap(p.dirname(p.abspath(__file__)) + '/img/icons/website.png')

        cs = (0.299 * window_color.redF() +
            0.587 * window_color.greenF() +
            0.114 * window_color.blueF())
        if cs < 0.5:
            return dark_github_icon, dark_website_icon
        else:
            return light_github_icon, light_website_icon