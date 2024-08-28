# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QtDesigner.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.boton_ac = QPushButton(Form)
        self.boton_ac.setObjectName(u"boton_ac")
        self.boton_ac.setGeometry(QRect(70, 100, 51, 24))
        self.boton_cambio_signo = QPushButton(Form)
        self.boton_cambio_signo.setObjectName(u"boton_cambio_signo")
        self.boton_cambio_signo.setGeometry(QRect(120, 100, 51, 24))
        self.boton_porciento = QPushButton(Form)
        self.boton_porciento.setObjectName(u"boton_porciento")
        self.boton_porciento.setGeometry(QRect(170, 100, 51, 24))
        self.boton_dividido = QPushButton(Form)
        self.boton_dividido.setObjectName(u"boton_dividido")
        self.boton_dividido.setGeometry(QRect(220, 100, 51, 24))
        self.boton_multiplicacion = QPushButton(Form)
        self.boton_multiplicacion.setObjectName(u"boton_multiplicacion")
        self.boton_multiplicacion.setGeometry(QRect(220, 120, 51, 24))
        self.boton_7 = QPushButton(Form)
        self.boton_7.setObjectName(u"boton_7")
        self.boton_7.setGeometry(QRect(70, 120, 51, 24))
        self.boton_8 = QPushButton(Form)
        self.boton_8.setObjectName(u"boton_8")
        self.boton_8.setGeometry(QRect(120, 120, 51, 24))
        self.boton_9 = QPushButton(Form)
        self.boton_9.setObjectName(u"boton_9")
        self.boton_9.setGeometry(QRect(170, 120, 51, 24))
        self.boton_menos = QPushButton(Form)
        self.boton_menos.setObjectName(u"boton_menos")
        self.boton_menos.setGeometry(QRect(220, 140, 51, 24))
        self.boton_1 = QPushButton(Form)
        self.boton_1.setObjectName(u"boton_1")
        self.boton_1.setGeometry(QRect(70, 160, 51, 24))
        self.boton_4 = QPushButton(Form)
        self.boton_4.setObjectName(u"boton_4")
        self.boton_4.setGeometry(QRect(70, 140, 51, 24))
        self.boton_3 = QPushButton(Form)
        self.boton_3.setObjectName(u"boton_3")
        self.boton_3.setGeometry(QRect(170, 160, 51, 24))
        self.boton_5 = QPushButton(Form)
        self.boton_5.setObjectName(u"boton_5")
        self.boton_5.setGeometry(QRect(120, 140, 51, 24))
        self.boton_suma = QPushButton(Form)
        self.boton_suma.setObjectName(u"boton_suma")
        self.boton_suma.setGeometry(QRect(220, 160, 51, 24))
        self.boton_6 = QPushButton(Form)
        self.boton_6.setObjectName(u"boton_6")
        self.boton_6.setGeometry(QRect(170, 140, 51, 24))
        self.boton_2 = QPushButton(Form)
        self.boton_2.setObjectName(u"boton_2")
        self.boton_2.setGeometry(QRect(120, 160, 51, 24))
        self.boton_0 = QPushButton(Form)
        self.boton_0.setObjectName(u"boton_0")
        self.boton_0.setGeometry(QRect(70, 180, 101, 24))
        self.boton_igual = QPushButton(Form)
        self.boton_igual.setObjectName(u"boton_igual")
        self.boton_igual.setGeometry(QRect(220, 180, 51, 24))
        self.boton_coma = QPushButton(Form)
        self.boton_coma.setObjectName(u"boton_coma")
        self.boton_coma.setGeometry(QRect(170, 180, 51, 24))
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(70, 60, 201, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.boton_ac.setText(QCoreApplication.translate("Form", u"AC", None))
        self.boton_cambio_signo.setText(QCoreApplication.translate("Form", u"+/-", None))
        self.boton_porciento.setText(QCoreApplication.translate("Form", u"%", None))
        self.boton_dividido.setText(QCoreApplication.translate("Form", u"/", None))
        self.boton_multiplicacion.setText(QCoreApplication.translate("Form", u"*", None))
        self.boton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.boton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.boton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.boton_menos.setText(QCoreApplication.translate("Form", u"-", None))
        self.boton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.boton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.boton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.boton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.boton_suma.setText(QCoreApplication.translate("Form", u"+", None))
        self.boton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.boton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.boton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.boton_igual.setText(QCoreApplication.translate("Form", u"=", None))
        self.boton_coma.setText(QCoreApplication.translate("Form", u",", None))
    # retranslateUi

