# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QTD6.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(False)
        MainWindow.resize(1000, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(80)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1000, 800))
        MainWindow.setMaximumSize(QSize(1002, 800))
        MainWindow.setBaseSize(QSize(1000, 800))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255))")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.description = QLabel(self.centralwidget)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(10, 10, 461, 131))

        self.change_button = QPushButton(self.centralwidget)
        self.change_button.setObjectName(u"change_button")
        self.change_button.setGeometry(QRect(850, 10, 141, 61))
        font = QFont()
        font.setFamilies([u"Arial Narrow"])
        self.change_button.setFont(font)

        self.serch_button = QPushButton(self.centralwidget)
        self.serch_button.setObjectName(u"serch_button")
        self.serch_button.setGeometry(QRect(850, 80, 141, 61))

        self.find_folder = QLabel(self.centralwidget)
        self.find_folder.setObjectName(u"find_folder")
        self.find_folder.setGeometry(QRect(550, 80, 291, 61))

        self.target_path_text = QLabel(self.centralwidget)
        self.target_path_text.setObjectName(u"target_path_text")
        self.target_path_text.setGeometry(QRect(550, 10, 291, 61))
        self.target_path_text.setStyleSheet(u"background-color: white;")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u041e\u0418\u0421\u041a \u0421\u0423\u0414\u041d\u0410", None))
        self.description.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.change_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438 \u043f\u0430\u043f\u043a\u0443 \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.serch_button.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0421\u041a\u0410\u0422\u042c", None))
        self.find_folder.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043a\u0443\u044e \u043f\u0430\u043f\u043a\u0443 \u0438\u0441\u043a\u0430\u0442\u044c?", None))
        self.target_path_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u0430\u043f\u043a\u0430 \u043f\u043e\u0438\u0441\u043a\u0430 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e:</p><p>(\u0432\u044b\u0431\u0440\u0430\u043d\u0430 - \u043f\u0430\u0440\u043e\u0445\u043e\u0434\u044b \u0438 \u0447\u0435\u0440\u0442\u0435\u0436\u0438)</p></body></html>", None))
    # retranslateUi

