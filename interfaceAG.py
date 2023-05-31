# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AG.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        Form.setStyleSheet(u"QPushButton,\n"
"QLineEdit,\n"
"QPlainTextEdit {\n"
"border: 1px solid black;\n"
"border-radius: 8px;\n"
"font-size:16px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPlainTextEdit {border-radius: 2px;  text-align: justify;}")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 120, 239, 29))
        font = QFont()
        font.setPointSize(32)
        self.label_6.setFont(font)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 30, 104, 29))
        self.label_7.setFont(font)
        self.TAM = QLineEdit(Form)
        self.TAM.setObjectName(u"TAM")
        self.TAM.setGeometry(QRect(150, 30, 81, 31))
        self.TAM.setBaseSize(QSize(70, 20))
        self.Result = QPlainTextEdit(Form)
        self.Result.setObjectName(u"Result")
        self.Result.setGeometry(QRect(311, 108, 300, 261))
        font1 = QFont()
        self.Result.setFont(font1)
        self.Result.setStyleSheet(u"")
        self.Result.setReadOnly(True)
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(390, 70, 151, 29))
        self.label_8.setFont(font)
        self.btnResult = QPushButton(Form)
        self.btnResult.setObjectName(u"btnResult")
        self.btnResult.setGeometry(QRect(30, 400, 127, 35))
        self.btnResult.setFont(font1)
        self.btnResult.setStyleSheet(u"")
        self.btnResult.setIconSize(QSize(32, 32))
        self.btnResult.setAutoDefault(False)
        self.btnResultDefault = QPushButton(Form)
        self.btnResultDefault.setObjectName(u"btnResultDefault")
        self.btnResultDefault.setGeometry(QRect(165, 400, 149, 35))
        self.btnResultDefault.setFont(font1)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(44, 193, 173, 22))
        self.label_2.setMaximumSize(QSize(300, 100))
        self.label_2.setBaseSize(QSize(7, 50))
        font2 = QFont()
        font2.setPointSize(18)
        self.label_2.setFont(font2)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(24, 161, 193, 22))
        self.label.setMaximumSize(QSize(300, 100))
        self.label.setBaseSize(QSize(7, 50))
        self.label.setFont(font2)
        self.NG = QLineEdit(Form)
        self.NG.setObjectName(u"NG")
        self.NG.setGeometry(QRect(225, 193, 70, 25))
        self.NG.setBaseSize(QSize(70, 20))
        self.TP = QLineEdit(Form)
        self.TP.setObjectName(u"TP")
        self.TP.setEnabled(True)
        self.TP.setGeometry(QRect(225, 161, 70, 25))
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TP.sizePolicy().hasHeightForWidth())
        self.TP.setSizePolicy(sizePolicy)
        self.TP.setMaximumSize(QSize(70, 50))
        self.TP.setFont(font1)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(11, 225, 206, 22))
        self.label_3.setMaximumSize(QSize(300, 100))
        self.label_3.setBaseSize(QSize(7, 50))
        self.label_3.setFont(font2)
        self.TC = QLineEdit(Form)
        self.TC.setObjectName(u"TC")
        self.TC.setGeometry(QRect(225, 225, 70, 25))
        self.TC.setBaseSize(QSize(70, 20))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(74, 257, 143, 22))
        self.label_4.setMaximumSize(QSize(300, 100))
        self.label_4.setBaseSize(QSize(7, 50))
        self.label_4.setFont(font2)
        self.TM = QLineEdit(Form)
        self.TM.setObjectName(u"TM")
        self.TM.setGeometry(QRect(225, 257, 70, 25))
        self.TM.setBaseSize(QSize(70, 20))
        self.IG = QLineEdit(Form)
        self.IG.setObjectName(u"IG")
        self.IG.setGeometry(QRect(225, 289, 70, 25))
        self.IG.setBaseSize(QSize(70, 20))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(43, 289, 169, 22))
        self.label_5.setMaximumSize(QSize(300, 100))
        self.label_5.setBaseSize(QSize(7, 50))
        self.label_5.setFont(font2)

        self.retranslateUi(Form)

        self.btnResult.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:24pt;\">Configura\u00e7\u00e3o Gen\u00e9tico</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:24pt;\">Tamanho:</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Resposta Final</span></p></body></html>", None))
        self.btnResult.setText(QCoreApplication.translate("Form", u"Resultado", None))
        self.btnResultDefault.setText(QCoreApplication.translate("Form", u"Pr\u00e9 conf. Resultado", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"N\u00famero da gera\u00e7\u00f5es:", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tamanho da popula\u00e7\u00e3o:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Tamanho do cruzamento:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Taxa da muta\u00e7\u00e3o:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Intervalo de gera\u00e7\u00e3o:", None))
    # retranslateUi

