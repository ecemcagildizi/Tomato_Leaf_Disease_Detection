# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableView, QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        Widget.setStyleSheet(u"background-color: #8fa470;")
        self.widget_history = QWidget(Widget)
        self.widget_history.setObjectName(u"widget_history")
        self.widget_history.setGeometry(QRect(0, 0, 801, 261))
        self.widget_history.setStyleSheet(u"background-color: #8fa470;")
        self.pushButton = QPushButton(self.widget_history)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(700, 0, 100, 32))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius:5px;\n"
"background-color: #8fa470;\n"
"color:black;\n"
"font: 12pt \"Georgia\";\n"
"padding-right:5px;\n"
"padding-left:5px;\n"
"}")
        self.label = QLabel(self.widget_history)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 171, 20))
        self.label.setStyleSheet(u"color:black;\n"
"font: 12pt \"Georgia\";")
        self.tableView = QTableView(self.widget_history)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 40, 731, 181))
        self.tableView.setStyleSheet(u"color:black;")

        
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)   
        self.tableView.verticalHeader().setDefaultSectionSize(40)                    
        font = QFont("Georgia", 12)
        self.tableView.setFont(font)                                                  
        self.tableView.setAlternatingRowColors(True)                                  
        self.tableView.setStyleSheet("""
        QTableView {
        background-color: #8fa470;
        alternate-background-color: #8fa470;
        gridline-color: black;
        font: 12pt "Georgia";
        color: black;
        }
        QHeaderView::section {
        background-color: #8fa470;
        color: black;
        font: bold 12pt "Georgia";
        border: 1px solid black;
        padding: 4px;
        }
        """)

        self.pushButton_2_visible = QPushButton(self.widget_history)
        self.pushButton_2_visible.setObjectName(u"pushButton_2_visible")
        self.pushButton_2_visible.setGeometry(QRect(20, 220, 321, 32))
        self.pushButton_2_visible.setStyleSheet(u"QPushButton{\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius:5px;\n"
"background-color: #8fa470;\n"
"color:black;\n"
"font: 12pt \"Georgia\";\n"
"padding-right:5px;\n"
"padding-left:5px;\n"
"}")
        self.widget_predict = QWidget(Widget)
        self.widget_predict.setObjectName(u"widget_predict")
        self.widget_predict.setGeometry(QRect(0, 260, 801, 341))
        self.widget_predict.setStyleSheet(u"background-color: #8fa470;")
        self.pushButton_predict = QPushButton(self.widget_predict)
        self.pushButton_predict.setObjectName(u"pushButton_predict")
        self.pushButton_predict.setGeometry(QRect(230, 160, 491, 32))
        self.pushButton_predict.setStyleSheet(u"QPushButton{\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius:5px;\n"
"background-color: #8fa470;\n"
"color:black;\n"
"font: 12pt \"Georgia\";\n"
"padding-right:5px;\n"
"padding-left:5px;\n"
"}")
        self.label_image = QLabel(self.widget_predict)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(290, 0, 391, 161))
        self.label_image.setStyleSheet(u"QLabel {\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;         \n"
"}")
        self.label_result = QLabel(self.widget_predict)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setGeometry(QRect(140, 210, 481, 16))
        self.label_result.setStyleSheet(u"color:black;")
        self.textEdit_advice = QTextEdit(self.widget_predict)
        self.textEdit_advice.setObjectName(u"textEdit_advice")
        self.textEdit_advice.setGeometry(QRect(140, 240, 541, 111))
        self.textEdit_advice.setStyleSheet(u"QTextEdit {\n"
"    border: 2px solid rgb(0,0,0);\n"
"    border-radius: 5px;\n"
"    background-color: #8fa470; \n"
"    color: black;\n"
"    font: 12pt \"Georgia\";\n"
"    padding: 5px;\n"
"}")
        self.pushButton_load = QPushButton(self.widget_predict)
        self.pushButton_load.setObjectName(u"pushButton_load")
        self.pushButton_load.setGeometry(QRect(0, 10, 161, 32))
        self.pushButton_load.setStyleSheet(u"QPushButton{\n"
"border: 2px solid rgb(0,0,0);\n"
"border-radius:5px;\n"
"background-color: #8fa470;\n"
"color:black;\n"
"font: 12pt \"Georgia\";\n"
"padding-right:5px;\n"
"padding-left:5px;\n"
"}")

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
  

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Sign Out", None))
        self.label.setText(QCoreApplication.translate("Widget", u"History", None))
        self.pushButton_2_visible.setText(QCoreApplication.translate("Widget", u"Check Leaf Status", None))
        self.pushButton_predict.setText(QCoreApplication.translate("Widget", u"Predict", None))
        self.label_image.setText("")
        self.label_result.setText("")
        self.pushButton_load.setText(QCoreApplication.translate("Widget", u"Select Image", None))

