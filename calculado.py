# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 186)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.boton8 = QPushButton(Form)
        self.boton8.setObjectName(u"boton8")

        self.gridLayout.addWidget(self.boton8, 3, 1, 1, 1)

        self.boton1 = QPushButton(Form)
        self.boton1.setObjectName(u"boton1")

        self.gridLayout.addWidget(self.boton1, 1, 0, 1, 1)

        self.boton_resta = QPushButton(Form)
        self.boton_resta.setObjectName(u"boton_resta")

        self.gridLayout.addWidget(self.boton_resta, 2, 3, 1, 1)

        self.boton5 = QPushButton(Form)
        self.boton5.setObjectName(u"boton5")

        self.gridLayout.addWidget(self.boton5, 2, 1, 1, 1)

        self.boton6 = QPushButton(Form)
        self.boton6.setObjectName(u"boton6")

        self.gridLayout.addWidget(self.boton6, 2, 2, 1, 1)

        self.boton9 = QPushButton(Form)
        self.boton9.setObjectName(u"boton9")

        self.gridLayout.addWidget(self.boton9, 3, 2, 1, 1)

        self.boton2 = QPushButton(Form)
        self.boton2.setObjectName(u"boton2")

        self.gridLayout.addWidget(self.boton2, 1, 1, 1, 1)

        self.boton3 = QPushButton(Form)
        self.boton3.setObjectName(u"boton3")

        self.gridLayout.addWidget(self.boton3, 1, 2, 1, 1)

        self.boton_multiplicacion = QPushButton(Form)
        self.boton_multiplicacion.setObjectName(u"boton_multiplicacion")

        self.gridLayout.addWidget(self.boton_multiplicacion, 3, 3, 1, 1)

        self.boton_suma = QPushButton(Form)
        self.boton_suma.setObjectName(u"boton_suma")

        self.gridLayout.addWidget(self.boton_suma, 1, 3, 1, 1)

        self.layout_resultado = QLineEdit(Form)
        self.layout_resultado.setObjectName(u"layout_resultado")

        self.gridLayout.addWidget(self.layout_resultado, 0, 0, 1, 4)

        self.boton7 = QPushButton(Form)
        self.boton7.setObjectName(u"boton7")

        self.gridLayout.addWidget(self.boton7, 3, 0, 1, 1)

        self.boton4 = QPushButton(Form)
        self.boton4.setObjectName(u"boton4")

        self.gridLayout.addWidget(self.boton4, 2, 0, 1, 1)

        self.boton0 = QPushButton(Form)
        self.boton0.setObjectName(u"boton0")

        self.gridLayout.addWidget(self.boton0, 4, 0, 1, 1)

        self.boton_borrar = QPushButton(Form)
        self.boton_borrar.setObjectName(u"boton_borrar")

        self.gridLayout.addWidget(self.boton_borrar, 4, 1, 1, 1)

        self.boton_resultado = QPushButton(Form)
        self.boton_resultado.setObjectName(u"boton_resultado")

        self.gridLayout.addWidget(self.boton_resultado, 4, 2, 1, 1)

        self.boton_division = QPushButton(Form)
        self.boton_division.setObjectName(u"boton_division")

        self.gridLayout.addWidget(self.boton_division, 4, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.boton8.setText(QCoreApplication.translate("Form", u"8", None))
        self.boton1.setText(QCoreApplication.translate("Form", u"1", None))
        self.boton_resta.setText(QCoreApplication.translate("Form", u"-", None))
        self.boton5.setText(QCoreApplication.translate("Form", u"5", None))
        self.boton6.setText(QCoreApplication.translate("Form", u"6", None))
        self.boton9.setText(QCoreApplication.translate("Form", u"9", None))
        self.boton2.setText(QCoreApplication.translate("Form", u"2", None))
        self.boton3.setText(QCoreApplication.translate("Form", u"3", None))
        self.boton_multiplicacion.setText(QCoreApplication.translate("Form", u"*", None))
        self.boton_suma.setText(QCoreApplication.translate("Form", u"+", None))
        self.boton7.setText(QCoreApplication.translate("Form", u"7", None))
        self.boton4.setText(QCoreApplication.translate("Form", u"4", None))
        self.boton0.setText(QCoreApplication.translate("Form", u"0", None))
        self.boton_borrar.setText(QCoreApplication.translate("Form", u"AC", None))
        self.boton_resultado.setText(QCoreApplication.translate("Form", u"=", None))
        self.boton_division.setText(QCoreApplication.translate("Form", u"/", None))
    # retranslateUi

