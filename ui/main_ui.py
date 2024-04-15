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
        MainWindow.resize(412, 502)
        MainWindow.setMinimumSize(QSize(400, 480))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"background-color: #F5F5F5;")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.verticalWidget = QWidget(MainWindow)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(99)
        sizePolicy.setVerticalStretch(99)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setMaximumSize(QSize(1000, 1000))
        self.verticalWidget.setLayoutDirection(Qt.LeftToRight)
        self.vboxLayout = QVBoxLayout(self.verticalWidget)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.earned_money_label = QLabel(self.verticalWidget)
        self.earned_money_label.setObjectName(u"earned_money_label")
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

        self.horizontalLayout_3.addWidget(self.label_2)

        self.login_edit = QLineEdit(self.horizontalWidget)
        self.login_edit.setObjectName(u"login_edit")

        self.horizontalLayout_3.addWidget(self.login_edit)


        self.vboxLayout.addWidget(self.horizontalWidget)

        self.horizontalWidgetc = QWidget(self.verticalWidget)
        self.horizontalWidgetc.setObjectName(u"horizontalWidgetc")
        self.horizontalWidgetc.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalWidgetc)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.horizontalWidgetc)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.password_edit = QLineEdit(self.horizontalWidgetc)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_4.addWidget(self.password_edit)


        self.vboxLayout.addWidget(self.horizontalWidgetc)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.label_4 = QLabel(self.verticalWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout_6.addWidget(self.label_4)

        self.comboBox = QComboBox(self.verticalWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_6.addWidget(self.comboBox)


        self.vboxLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.vboxLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.start_bot_button = QPushButton(self.verticalWidget)
        self.start_bot_button.setObjectName(u"start_bot_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start_bot_button.sizePolicy().hasHeightForWidth())
        self.start_bot_button.setSizePolicy(sizePolicy1)
        self.start_bot_button.setMinimumSize(QSize(150, 30))
        self.start_bot_button.setMaximumSize(QSize(150, 30))
        self.start_bot_button.setStyleSheet(u"background-color: rgb(56, 169, 98);\n"
"color: #ffffff;\n"
"border-radius: 15px;")

        self.horizontalLayout_2.addWidget(self.start_bot_button)

        self.stop_bot_button = QPushButton(self.verticalWidget)
        self.stop_bot_button.setObjectName(u"stop_bot_button")
        self.stop_bot_button.setMinimumSize(QSize(150, 30))
        self.stop_bot_button.setMaximumSize(QSize(150, 30))
        self.stop_bot_button.setStyleSheet(u"background-color: #A93838;\n"
"color: #ffffff;\n"
"border-radius: 15px;")

        self.horizontalLayout_2.addWidget(self.stop_bot_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.vboxLayout.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout.addItem(self.horizontalSpacer)

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
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Browser", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Firefox", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Chrome", None))

        self.start_bot_button.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.stop_bot_button.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.log_box.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
    # retranslateUi

