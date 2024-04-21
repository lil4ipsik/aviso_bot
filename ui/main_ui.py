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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(400, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 400))
        MainWindow.setMaximumSize(QSize(400, 400))
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"background-color: #F5F5F5;")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.verticalWidget = QWidget(MainWindow)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(99)
        sizePolicy1.setVerticalStretch(99)
        sizePolicy1.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy1)
        self.verticalWidget.setMaximumSize(QSize(1000, 1000))
        self.verticalWidget.setLayoutDirection(Qt.LeftToRight)
        self.vboxLayout = QVBoxLayout(self.verticalWidget)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(self.verticalWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.earned_money_label = QLabel(self.verticalWidget)
        self.earned_money_label.setObjectName(u"earned_money_label")
        self.earned_money_label.setMinimumSize(QSize(104, 0))
        self.earned_money_label.setMaximumSize(QSize(104, 16777215))
        self.earned_money_label.setFont(font)

        self.horizontalLayout.addWidget(self.earned_money_label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.vboxLayout.addLayout(self.horizontalLayout)

        self.horizontalWidget = QWidget(self.verticalWidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.horizontalWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.login_edit = QLineEdit(self.horizontalWidget)
        self.login_edit.setObjectName(u"login_edit")

        self.horizontalLayout_3.addWidget(self.login_edit)

        self.label_3 = QLabel(self.horizontalWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.password_edit = QLineEdit(self.horizontalWidget)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.password_edit)


        self.vboxLayout.addWidget(self.horizontalWidget)

        self.horizontalWidget1 = QWidget(self.verticalWidget)
        self.horizontalWidget1.setObjectName(u"horizontalWidget1")
        self.horizontalWidget1.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.horizontalWidget1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.product_key_edit = QLineEdit(self.horizontalWidget1)
        self.product_key_edit.setObjectName(u"product_key_edit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.product_key_edit.sizePolicy().hasHeightForWidth())
        self.product_key_edit.setSizePolicy(sizePolicy2)
        self.product_key_edit.setMinimumSize(QSize(0, 0))
        self.product_key_edit.setMaximumSize(QSize(185, 16777215))
        self.product_key_edit.setMaxLength(29)
        self.product_key_edit.setAlignment(Qt.AlignCenter)
        self.product_key_edit.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.product_key_edit)

        self.vaild_label = QLabel(self.horizontalWidget1)
        self.vaild_label.setObjectName(u"vaild_label")
        self.vaild_label.setMinimumSize(QSize(120, 0))
        self.vaild_label.setMaximumSize(QSize(120, 16777215))
        self.vaild_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.vaild_label)


        self.vboxLayout.addWidget(self.horizontalWidget1)

        self.horizontalWidget2 = QWidget(self.verticalWidget)
        self.horizontalWidget2.setObjectName(u"horizontalWidget2")
        self.horizontalWidget2.setMinimumSize(QSize(50, 50))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalWidget2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.horizontalWidget2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.web_site_combo = QComboBox(self.horizontalWidget2)
        self.web_site_combo.addItem("")
        self.web_site_combo.addItem("")
        self.web_site_combo.setObjectName(u"web_site_combo")

        self.horizontalLayout_5.addWidget(self.web_site_combo)


        self.vboxLayout.addWidget(self.horizontalWidget2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.label_4 = QLabel(self.verticalWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(47, 16777215))

        self.horizontalLayout_6.addWidget(self.label_4)

        self.comboBox = QComboBox(self.verticalWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_6.addWidget(self.comboBox)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.start_bot_button = QPushButton(self.verticalWidget)
        self.start_bot_button.setObjectName(u"start_bot_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.start_bot_button.sizePolicy().hasHeightForWidth())
        self.start_bot_button.setSizePolicy(sizePolicy3)
        self.start_bot_button.setMinimumSize(QSize(60, 30))
        self.start_bot_button.setMaximumSize(QSize(150, 30))
        self.start_bot_button.setStyleSheet(u"background-color: rgb(56, 169, 98);\n"
"color: #ffffff;\n"
"border-radius: 15px;")

        self.horizontalLayout_2.addWidget(self.start_bot_button)

        self.stop_bot_button = QPushButton(self.verticalWidget)
        self.stop_bot_button.setObjectName(u"stop_bot_button")
        self.stop_bot_button.setMinimumSize(QSize(60, 30))
        self.stop_bot_button.setMaximumSize(QSize(150, 30))
        self.stop_bot_button.setStyleSheet(u"background-color: #A93838;\n"
"color: #ffffff;\n"
"border-radius: 15px;")

        self.horizontalLayout_2.addWidget(self.stop_bot_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.status_label = QLabel(self.verticalWidget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.status_label)


        self.horizontalLayout_6.addLayout(self.verticalLayout)


        self.vboxLayout.addLayout(self.horizontalLayout_6)

        self.label_6 = QLabel(self.verticalWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.vboxLayout.addWidget(self.label_6)

        self.log_box = QTextEdit(self.verticalWidget)
        self.log_box.setObjectName(u"log_box")
        self.log_box.setStyleSheet(u"border: none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.log_box.setReadOnly(True)
        self.log_box.setOverwriteMode(True)

        self.vboxLayout.addWidget(self.log_box)

        MainWindow.setCentralWidget(self.verticalWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"aviso.bz bot", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total earned:", None))
        self.earned_money_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Login      ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Key", None))
        self.product_key_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter product key (or add it to .env)", None))
        self.vaild_label.setText(QCoreApplication.translate("MainWindow", u"Valid until 0000-00-00", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"WebSite", None))
        self.web_site_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Aviso", None))
        self.web_site_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Profitcentr", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Browser", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Firefox", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Chrome", None))

        self.start_bot_button.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.stop_bot_button.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Status: Idle", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Request a free testing key for 7 days on https://aviso.xserv.pp.ua", None))
        self.log_box.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

