# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(80)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1000, 800))
        MainWindow.setMaximumSize(QSize(1002, 800))
        MainWindow.setBaseSize(QSize(1000, 800))
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(Qt.PreventContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255))")
        MainWindow.setIconSize(QSize(40, 40))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_refresh_data = QPushButton(self.centralwidget)
        self.btn_refresh_data.setObjectName(u"btn_refresh_data")
        self.btn_refresh_data.setGeometry(QRect(790, 30, 171, 61))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.btn_refresh_data.setFont(font1)
        self.btn_refresh_data.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:10px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.lbl_time_save = QLabel(self.centralwidget)
        self.lbl_time_save.setObjectName(u"lbl_time_save")
        self.lbl_time_save.setGeometry(QRect(580, 20, 221, 31))
        self.lbl_time_save.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 9pt;\n"
"background-color: none;\n"
"border: none;")
        self.lbl_time_save.setMargin(5)
        self.btn_search_folder = QPushButton(self.centralwidget)
        self.btn_search_folder.setObjectName(u"btn_search_folder")
        self.btn_search_folder.setEnabled(True)
        self.btn_search_folder.setGeometry(QRect(350, 140, 161, 61))
        self.btn_search_folder.setFont(font1)
        self.btn_search_folder.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 2px solid rgba(255,255,255,60);\n"
"     border-radius:10px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.btn_search_folder.setIconSize(QSize(32, 32))
        self.lbl_target_path = QLabel(self.centralwidget)
        self.lbl_target_path.setObjectName(u"lbl_target_path")
        self.lbl_target_path.setGeometry(QRect(20, 20, 321, 31))
        self.lbl_target_path.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 9pt;\n"
"background-color: none;\n"
"border: none;")
        self.lbl_target_path.setMargin(5)
        self.lbl_result = QLabel(self.centralwidget)
        self.lbl_result.setObjectName(u"lbl_result")
        self.lbl_result.setGeometry(QRect(10, 580, 981, 211))
        self.lbl_result.setFont(font)
        self.lbl_last_query = QLabel(self.centralwidget)
        self.lbl_last_query.setObjectName(u"lbl_last_query")
        self.lbl_last_query.setGeometry(QRect(580, 140, 191, 61))
        self.lbl_last_query.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 9pt;\n"
"background-color: none;\n"
"border: none;")
        self.btn_last_req = QPushButton(self.centralwidget)
        self.btn_last_req.setObjectName(u"btn_last_req")
        self.btn_last_req.setGeometry(QRect(790, 140, 171, 61))
        self.btn_last_req.setFont(font1)
        self.btn_last_req.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:10px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/search_FILL0_wght400_GRAD0_opsz40.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_last_req.setIcon(icon)
        self.btn_last_req.setIconSize(QSize(32, 32))
        self.cb_folder = QComboBox(self.centralwidget)
        self.cb_folder.addItem("")
        self.cb_folder.addItem("")
        self.cb_folder.setObjectName(u"cb_folder")
        self.cb_folder.setGeometry(QRect(20, 60, 321, 29))
        self.cb_folder.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"    color: black;\n"
"}")
        self.dt_time_save = QDateTimeEdit(self.centralwidget)
        self.dt_time_save.setObjectName(u"dt_time_save")
        self.dt_time_save.setGeometry(QRect(580, 60, 194, 31))
        self.le_target = QLineEdit(self.centralwidget)
        self.le_target.setObjectName(u"le_target")
        self.le_target.setGeometry(QRect(20, 140, 321, 61))
        self.le_target.setStyleSheet(u"font-size: 20pt;\n"
"color: white;\n"
"padding-left: 10px;")
        self.lst_result = QListWidget(self.centralwidget)
        self.lst_result.setObjectName(u"lst_result")
        self.lst_result.setGeometry(QRect(50, 240, 911, 291))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u041e\u0418\u0421\u041a \u0421\u0423\u0414\u041d\u0410", None))
        self.btn_refresh_data.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0411\u041d\u041e\u0412\u0418\u0422\u042c \n"
"\u0414\u0410\u041d\u041d\u042b\u0415 \u0412 \u0411\u0410\u0417\u0415", None))
        self.lbl_time_save.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0414\u0430\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0444\u0430\u0439\u043b\u0430:</p><p>\u0445\u0445</p></body></html>", None))
        self.btn_search_folder.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0421\u041a\u0410\u0422\u042c", None))
        self.lbl_target_path.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u0430\u043f\u043a\u0430 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e: &quot;03_\u043f\u0430\u0440\u043e\u0445\u043e\u0434\u044b_\u0447\u0435\u0440\u0442\u0435\u0436\u0438&quot;</p></body></html>", None))
        self.lbl_result.setText("")
        self.lbl_last_query.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 \u0437\u0430\u043f\u0440\u043e\u0441\u044b", None))
        self.btn_last_req.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0422\u041a\u0420\u042b\u0422\u042c", None))
        self.cb_folder.setItemText(0, QCoreApplication.translate("MainWindow", u"03_\u043f\u0430\u0440\u043e\u0445\u043e\u0434\u044b_\u0447\u0435\u0440\u0442\u0435\u0436\u0438", None))
        self.cb_folder.setItemText(1, QCoreApplication.translate("MainWindow", u"02 Library", None))

        self.cb_folder.setProperty("placeholderText", QCoreApplication.translate("MainWindow", u"Choose status", None))
        self.le_target.setText("")
        self.le_target.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0427\u0442\u043e \u0438\u0449\u0435\u043c?", None))
    # retranslateUi

