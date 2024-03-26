# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm_folder.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(377, 345)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255))")
        self.btn_conf_folder = QPushButton(Dialog)
        self.btn_conf_folder.setObjectName(u"btn_conf_folder")
        self.btn_conf_folder.setGeometry(QRect(110, 180, 161, 61))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.btn_conf_folder.setFont(font)
        self.btn_conf_folder.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color:rgb(255, 126, 87);\n"
"border: 3px solid rgba(255,255,255,40);\n"
"border-radius: 10px;")
        self.btn_conf_folder.setIconSize(QSize(32, 32))
        self.line_conf_folder = QLineEdit(Dialog)
        self.line_conf_folder.setObjectName(u"line_conf_folder")
        self.line_conf_folder.setGeometry(QRect(10, 120, 361, 51))
        self.line_conf_folder.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_conf_folder.setText(QCoreApplication.translate("Dialog", u"\u041f\u041e\u0414\u0422\u0412\u0415\u0420\u0414\u0418\u0422\u042c", None))
        self.line_conf_folder.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435  \u0438\u0441\u043a\u043e\u043c\u043e\u0439 \u043f\u0430\u043f\u043a\u0438", None))
    # retranslateUi

