# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QSize(800, 480))
        MainWindow.setMaximumSize(QSize(800, 480))
        MainWindow.setStyleSheet(u"background-color: #2c824c;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 90, 550, 60))
        font = QFont()
        font.setFamilies([u"Furore"])
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 35pt \"Furore\";\n"
"background: transparent;\n"
"")
        self.label.setInputMethodHints(Qt.ImhNone)
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(1)
        self.label.setAlignment(Qt.AlignCenter)
        self.password_input = QLineEdit(self.centralwidget)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(245, 207, 310, 43))
        self.password_input.setStyleSheet(u"border-radius: 15%;\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"Furore\";\n"
"padding-left: 25px;\n"
"padding-right: 25px;\n"
"background: rgba(255, 255, 255, 0.3);")
        self.password_input.setMaxLength(10)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setAlignment(Qt.AlignCenter)
        self._ = QPushButton(self.centralwidget)
        self._.setObjectName(u"_")
        self._.setGeometry(QRect(-6, -7, 811, 491))
        self._.setStyleSheet(u"border-radius: 10%;\n"
"background-image: url(:/photo/no-wifi.png);\n"
"background: transparent;")
        self.forgot_password_button = QPushButton(self.centralwidget)
        self.forgot_password_button.setObjectName(u"forgot_password_button")
        self.forgot_password_button.setGeometry(QRect(190, 326, 341, 81))
        self.forgot_password_button.setStyleSheet(u"border-radius: 13%;\n"
"background: #ffffff;\n"
"color: #38A962;\n"
"font: 20pt \"Furore\";")
        self.login_button = QPushButton(self.centralwidget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(302, 326, 196, 81))
        self.login_button.setStyleSheet(u"border-radius: 13%;\n"
"background: #ffffff;\n"
"color: #38A962;\n"
"font: 20pt \"Furore\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(19, 18, 34, 52))
        self.label_2.setStyleSheet(u"background-image: url(:/photo/polysia_icon.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.hide_show_password_icon = QLabel(self.centralwidget)
        self.hide_show_password_icon.setObjectName(u"hide_show_password_icon")
        self.hide_show_password_icon.setGeometry(QRect(490, 207, 51, 43))
        self.hide_show_password_icon.setStyleSheet(u"background-color: none;\n"
"background-image: url(:/photo/\uf06e.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.update_app_button = QPushButton(self.centralwidget)
        self.update_app_button.setObjectName(u"update_app_button")
        self.update_app_button.setGeometry(QRect(649, 30, 131, 41))
        self.update_app_button.setStyleSheet(u"border-radius: 13%;\n"
"background: #ffffff;\n"
"color: #38A962;\n"
"font: 14pt \"Furore\";")
        self.battery_level_label = QLabel(self.centralwidget)
        self.battery_level_label.setObjectName(u"battery_level_label")
        self.battery_level_label.setGeometry(QRect(744, 0, 60, 16))
        self.battery_level_label.setStyleSheet(u"background: transparent;\n"
"color: #ffffff;\n"
"font: 14pt \"Furore\";")
        self.battery_level_label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self._.raise_()
        self.password_input.raise_()
        self.label.raise_()
        self.forgot_password_button.raise_()
        self.login_button.raise_()
        self.hide_show_password_icon.raise_()
        self.update_app_button.raise_()
        self.label_2.raise_()
        self.battery_level_label.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0412\u0406\u0419\u0414\u0406\u0422\u042c \u0412 \u0421\u0418\u0421\u0422\u0415\u041c\u0423:", None))
        self.password_input.setText("")
        self.password_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0412\u0415\u0414\u0406\u0422\u042c \u041f\u0410\u0420\u041e\u041b\u042c", None))
        self._.setText("")
        self.forgot_password_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0431\u0443\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c?", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0432\u0456\u0439\u0442\u0438", None))
        self.label_2.setText("")
        self.hide_show_password_icon.setText("")
        self.update_app_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043d\u043e\u0432\u0438\u0442\u0438\u0441\u044c", None))
        self.battery_level_label.setText("")
    # retranslateUi

