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
import res-rc_rc

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
        MainWindow.setContextMenuPolicy(Qt.PreventContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255))")
        MainWindow.setIconSize(QSize(40, 40))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.refresh_data = QPushButton(self.centralwidget)
        self.refresh_data.setObjectName(u"refresh_data")
        self.refresh_data.setGeometry(QRect(820, 20, 171, 61))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.refresh_data.setFont(font)
        self.refresh_data.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color:rgb(255, 126, 87);\n"
"border: 3px solid rgba(255,255,255,40);\n"
"border-radius: 10px;")
        self.time_save = QLabel(self.centralwidget)
        self.time_save.setObjectName(u"time_save")
        self.time_save.setGeometry(QRect(590, 20, 221, 61))
        self.time_save.setStyleSheet(u"background-color: white;\n"
"font-family: arial narrow;\n"
"font-size: 11pt;")
        self.time_save.setMargin(5)
        self.seech_button = QPushButton(self.centralwidget)
        self.seech_button.setObjectName(u"seech_button")
        self.seech_button.setGeometry(QRect(340, 110, 161, 61))
        self.seech_button.setFont(font)
        self.seech_button.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color:rgb(255, 126, 87);\n"
"border: 3px solid rgba(255,255,255,40);\n"
"border-radius: 10px;")
        icon = QIcon()
        icon.addFile(u":/icon/icons/search_FILL0_wght400_GRAD0_opsz40.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.seech_button.setIcon(icon)
        self.seech_button.setIconSize(QSize(32, 32))
        self.change_folder = QPushButton(self.centralwidget)
        self.change_folder.setObjectName(u"change_folder")
        self.change_folder.setGeometry(QRect(340, 20, 161, 61))
        self.change_folder.setFont(font)
        self.change_folder.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color:rgb(255, 126, 87);\n"
"border: 3px solid rgba(255,255,255,40);\n"
"border-radius: 10px;")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/folder_FILL0_wght400_GRAD0_opsz40.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.change_folder.setIcon(icon1)
        self.change_folder.setIconSize(QSize(32, 32))
        self.find_folder = QLabel(self.centralwidget)
        self.find_folder.setObjectName(u"find_folder")
        self.find_folder.setGeometry(QRect(20, 110, 311, 62))
        self.find_folder.setStyleSheet(u"background-color: white;\n"
"font-family: arial narrow;\n"
"font-size: 11pt;")
        self.target_path_text = QLabel(self.centralwidget)
        self.target_path_text.setObjectName(u"target_path_text")
        self.target_path_text.setGeometry(QRect(20, 20, 311, 62))
        self.target_path_text.setStyleSheet(u"background-color: white;\n"
"font-family: arial narrow;\n"
"font-size: 11pt;")
        self.target_path_text.setMargin(5)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 600, 981, 191))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u041e\u0418\u0421\u041a \u0421\u0423\u0414\u041d\u0410", None))
        self.refresh_data.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0411\u041d\u041e\u0412\u0418\u0422\u042c \n"
"\u0414\u0410\u041d\u041d\u042b\u0415 \u0412 \u0411\u0410\u0417\u0415", None))
        self.time_save.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0414\u0430\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0444\u0430\u0439\u043b\u0430:</p><p>\u0445\u0445</p></body></html>", None))
        self.seech_button.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0421\u041a\u0410\u0422\u042c", None))
        self.change_folder.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0417\u041c\u0415\u041d\u0418\u0422\u042c", None))
        self.find_folder.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043a\u0443\u044e \u043f\u0430\u043f\u043a\u0443 (\u0441\u0443\u0434\u043d\u043e) \u0438\u0441\u043a\u0430\u0442\u044c?", None))
        self.target_path_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u0430\u043f\u043a\u0430 \u043f\u043e\u0438\u0441\u043a\u0430 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e:</p><p>&quot;03_\u043f\u0430\u0440\u043e\u0445\u043e\u0434\u044b_\u0447\u0435\u0440\u0442\u0435\u0436\u0438&quot;</p></body></html>", None))
        self.label.setText("")
    # retranslateUi

