# -*- coding: utf-8 -*-
from PySide6.QtCore import QCoreApplication, QRect, QMetaObject
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName("Widget")
        Widget.resize(800, 600)
        Widget.setStyleSheet("background-color: #8fa470;")

        self.widget = QWidget(Widget)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(90, 70, 611, 471))

        self.label = QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(240, 40, 141, 16))
        self.label.setText("SIGN IN PAGE")
        self.label.setStyleSheet("color: black; font: 18pt 'Georgia'; font-weight: bold;")

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(140, 130, 58, 16))
        self.label_2.setStyleSheet("color:black; font: 12pt 'Georgia';")

        self.lineEdit_email = QLineEdit(self.widget)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(200, 130, 311, 21))
        self.lineEdit_email.setStyleSheet("""
            QLineEdit {
                border: none;
                border-bottom: 2px solid rgb(0,0,0);
                padding-bottom: 2px;
                color: black;
                font: 12pt 'Georgia';
            }
        """)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(130, 190, 58, 16))
        self.label_3.setStyleSheet("color:black; font: 12pt 'Georgia';")

        self.lineEdit_password = QLineEdit(self.widget)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(200, 190, 311, 21))
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setStyleSheet("""
            QLineEdit {
                border: none;
                border-bottom: 2px solid rgb(0,0,0);
                padding-bottom: 2px;
                color: black;
                font: 12pt 'Georgia';
            }
        """)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(220, 290, 161, 32))
        self.pushButton.setText("Sign In")
        self.pushButton.setStyleSheet("""
            QPushButton {
                border: 2px solid rgb(0,0,0);
                border-radius:5px;
                background-color: #8fa470;
                color:black;
                font: 12pt 'Georgia';
                padding-left:5px;
                padding-right:5px;
            }
            QPushButton:hover {
                background-color: #9fbf6e;
            }
        """)

        QMetaObject.connectSlotsByName(Widget)

        self.retranslateUi(Widget)

    def retranslateUi(self, Widget):
        QCoreApplication.translate("Widget", "Widget", None)
        self.label_2.setText(QCoreApplication.translate("Widget", "E-Mail:", None))
        self.label_3.setText(QCoreApplication.translate("Widget", "Password:", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", "Sign In", None))
