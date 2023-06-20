# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ag.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
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
        self.label_6.setGeometry(QRect(0, 100, 311, 40))
        font = QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(15, 306, 288, 32))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(300, 100))
        self.label_5.setBaseSize(QSize(7, 50))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_5.setFont(font1)

        self.horizontalLayout.addWidget(self.label_5)

        self.IG = QLineEdit(self.widget)
        self.IG.setObjectName(u"IG")
        self.IG.setMaximumSize(QSize(70, 16777215))
        self.IG.setBaseSize(QSize(70, 20))

        self.horizontalLayout.addWidget(self.IG)

        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(15, 270, 251, 32))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(300, 100))
        self.label_4.setBaseSize(QSize(7, 50))
        self.label_4.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.TM = QLineEdit(self.widget1)
        self.TM.setObjectName(u"TM")
        self.TM.setMaximumSize(QSize(70, 16777215))
        self.TM.setBaseSize(QSize(70, 20))

        self.horizontalLayout_2.addWidget(self.TM)

        self.widget2 = QWidget(Form)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(15, 234, 330, 32))
        self.horizontalLayout_3 = QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(300, 100))
        self.label_3.setBaseSize(QSize(7, 50))
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.TC = QLineEdit(self.widget2)
        self.TC.setObjectName(u"TC")
        self.TC.setMaximumSize(QSize(70, 16777215))
        self.TC.setBaseSize(QSize(70, 20))

        self.horizontalLayout_3.addWidget(self.TC)

        self.widget3 = QWidget(Form)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(15, 198, 290, 32))
        self.horizontalLayout_4 = QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(300, 100))
        self.label_2.setBaseSize(QSize(7, 50))
        self.label_2.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.NG = QLineEdit(self.widget3)
        self.NG.setObjectName(u"NG")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.NG.sizePolicy().hasHeightForWidth())
        self.NG.setSizePolicy(sizePolicy1)
        self.NG.setMaximumSize(QSize(70, 50))
        self.NG.setBaseSize(QSize(70, 20))

        self.horizontalLayout_4.addWidget(self.NG)

        self.widget4 = QWidget(Form)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(15, 161, 315, 32))
        self.horizontalLayout_5 = QHBoxLayout(self.widget4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(300, 100))
        self.label.setBaseSize(QSize(7, 50))
        self.label.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label)

        self.TP = QLineEdit(self.widget4)
        self.TP.setObjectName(u"TP")
        self.TP.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.TP.sizePolicy().hasHeightForWidth())
        self.TP.setSizePolicy(sizePolicy1)
        self.TP.setMaximumSize(QSize(70, 50))
        font2 = QFont()
        self.TP.setFont(font2)

        self.horizontalLayout_5.addWidget(self.TP)

        self.widget5 = QWidget(Form)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setGeometry(QRect(350, 120, 258, 245))
        self.verticalLayout = QVBoxLayout(self.widget5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget5)
        self.label_8.setObjectName(u"label_8")
        font3 = QFont()
        font3.setPointSize(32)
        self.label_8.setFont(font3)

        self.verticalLayout.addWidget(self.label_8)

        self.Result = QPlainTextEdit(self.widget5)
        self.Result.setObjectName(u"Result")
        self.Result.setFont(font2)
        self.Result.setStyleSheet(u"")
        self.Result.setReadOnly(True)

        self.verticalLayout.addWidget(self.Result)

        self.widget6 = QWidget(Form)
        self.widget6.setObjectName(u"widget6")
        self.widget6.setGeometry(QRect(40, 30, 299, 47))
        self.horizontalLayout_6 = QHBoxLayout(self.widget6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.TAM = QLineEdit(self.widget6)
        self.TAM.setObjectName(u"TAM")
        self.TAM.setBaseSize(QSize(70, 20))

        self.horizontalLayout_6.addWidget(self.TAM)

        self.widget7 = QWidget(Form)
        self.widget7.setObjectName(u"widget7")
        self.widget7.setGeometry(QRect(30, 400, 232, 27))
        self.horizontalLayout_7 = QHBoxLayout(self.widget7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btnResult = QPushButton(self.widget7)
        self.btnResult.setObjectName(u"btnResult")
        self.btnResult.setFont(font2)
        self.btnResult.setStyleSheet(u"")
        self.btnResult.setIconSize(QSize(32, 32))
        self.btnResult.setAutoDefault(False)

        self.horizontalLayout_7.addWidget(self.btnResult)

        self.btnResultDefault = QPushButton(self.widget7)
        self.btnResultDefault.setObjectName(u"btnResultDefault")
        self.btnResultDefault.setFont(font2)

        self.horizontalLayout_7.addWidget(self.btnResultDefault)


        self.retranslateUi(Form)

        self.btnResult.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:22pt;\">Configura\u00e7\u00e3o Gen\u00e9tico</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Intervalo de gera\u00e7\u00e3o:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Taxa da muta\u00e7\u00e3o:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Tamanho do cruzamento:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"N\u00famero da gera\u00e7\u00f5es:", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tamanho da popula\u00e7\u00e3o:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Resposta Final</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:24pt;\">Tamanho:</span></p></body></html>", None))
        self.btnResult.setText(QCoreApplication.translate("Form", u"Resultado", None))
        self.btnResultDefault.setText(QCoreApplication.translate("Form", u"Pr\u00e9 conf. Resultado", None))
    # retranslateUi

