import sys
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLineEdit, QComboBox, QMainWindow, QTabWidget , QTreeWidget, QTreeWidgetItem
from PyQt6.QtGui import QIcon
import json
from userdata import add_user, delete_user_by_id, edit_user_by_id
from os import path as p

app_icon_path = p.dirname(p.abspath(__file__)) + '/icon.ico'

class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setFixedSize(600, 400)
        self.setWindowIcon(QIcon(app_icon_path))
        self.tab_widget = QTabWidget()

        users_tab = QWidget()
        about_tab = QWidget()

        self.tab_widget.addTab(users_tab, "Users")
        self.tab_widget.addTab(about_tab, "About")

        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabels(["ID", "Username", "Password", "Key", "Site"])
        self.load_user_data()

        buttons_layout = QHBoxLayout()
        add_button = QPushButton("Add")
        buttons_layout.addWidget(add_button)
        add_button.clicked.connect(self.add_user)
        edit_button = QPushButton("Edit")
        edit_button.setEnabled(False)
        edit_button.clicked.connect(lambda: self.edit_user(self.tree_widget.currentItem().text(0), self.tree_widget.currentItem().text(1), self.tree_widget.currentItem().text(2), self.tree_widget.currentItem().text(3), self.tree_widget.currentItem().text(4)))
        buttons_layout.addWidget(edit_button)
        remove_button = QPushButton("Remove")
        remove_button.setEnabled(False)
        remove_button.clicked.connect(self.delete_user)
        buttons_layout.addWidget(remove_button)

        self.tree_widget.itemClicked.connect(lambda item: [edit_button.setEnabled(True), remove_button.setEnabled(True)])
        self.tree_widget.itemDoubleClicked.connect(lambda item: [self.edit_user(item.text(0), item.text(1), item.text(2), item.text(3), item.text(4))]) 
        self.tree_widget.itemSelectionChanged.connect(lambda: [edit_button.setEnabled(False), remove_button.setEnabled(False)])

        users_layout = QVBoxLayout()
        users_layout.addWidget(self.tree_widget)
        users_layout.addLayout(buttons_layout)
        users_tab.setLayout(users_layout)

        label2 = QLabel("Content for Tab 2")
        layout2 = QVBoxLayout()
        layout2.addWidget(label2)
        about_tab.setLayout(layout2)

        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_user_data(self):
        try:
            with open('userdata/userdata.json', 'r') as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = {}

        self.tree_widget.clear()
        if user_data:
            for user_id, data in user_data.items():
                item = QTreeWidgetItem([user_id, data['username'], data['password'], data['key'], data['site']])
                self.tree_widget.addTopLevelItem(item)
        else:
            self.tree_widget.clear()

    def add_user(self):
        add_user_window = QWidget()
        add_user_window.setWindowTitle("Add user")
        add_user_window.setFixedSize(400, 200)
        add_user_window.setWindowIcon(QIcon(app_icon_path))

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
        key_edit.setMaxLength(29)
        key_layout.addWidget(key_label)
        key_layout.addWidget(key_edit)
        site_layout = QHBoxLayout()
        site_label = QLabel("Site:")
        site_combo = QComboBox()
        site_combo.addItem("Aviso")
        site_combo.addItem("Proficentr")
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
        selected_item = self.tree_widget.currentItem()
        if selected_item is not None:
            user_id = selected_item.text(0)
            print(f"Deleting user with ID {user_id}")
            delete_user_by_id(user_id)
            self.load_user_data()

    def edit_user(self, id, username, password, key, site):
        edit_user_window = QWidget()
        edit_user_window.setWindowTitle("Edit user")
        edit_user_window.setFixedSize(400, 200)
        edit_user_window.setWindowIcon(QIcon(app_icon_path))

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
        key_edit.setMaxLength(29)
        key_edit.setText(key)
        key_layout.addWidget(key_label)
        key_layout.addWidget(key_edit)
        site_layout = QHBoxLayout()
        site_label = QLabel("Site:")
        site_combo = QComboBox()
        site_combo.addItem("Aviso")
        site_combo.addItem("Proficentr")
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

        

app = QApplication(sys.argv)
window = SettingsWindow()
window.show()
sys.exit(app.exec())
