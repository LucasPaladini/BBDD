# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ListaTarea_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QListView,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setStyleSheet(u"background-color: rgb(199, 199, 199)")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ingresar_tarea = QLineEdit(Form)
        self.ingresar_tarea.setObjectName(u"ingresar_tarea")
        self.ingresar_tarea.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.ingresar_tarea, 0, 0, 1, 1)

        self.lista_pantalla = QListView(Form)
        self.lista_pantalla.setObjectName(u"lista_pantalla")

        self.gridLayout.addWidget(self.lista_pantalla, 4, 0, 1, 2)

        self.boton_eliminar_tarea = QPushButton(Form)
        self.boton_eliminar_tarea.setObjectName(u"boton_eliminar_tarea")

        self.gridLayout.addWidget(self.boton_eliminar_tarea, 7, 0, 1, 2)

        self.boton_agregar_tarea = QPushButton(Form)
        self.boton_agregar_tarea.setObjectName(u"boton_agregar_tarea")
        self.boton_agregar_tarea.setAutoDefault(False)
        self.boton_agregar_tarea.setFlat(False)

        self.gridLayout.addWidget(self.boton_agregar_tarea, 0, 1, 1, 1)

        self.boton_completar_tarea = QPushButton(Form)
        self.boton_completar_tarea.setObjectName(u"boton_completar_tarea")

        self.gridLayout.addWidget(self.boton_completar_tarea, 6, 0, 1, 2)


        self.retranslateUi(Form)

        self.boton_agregar_tarea.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        Form.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ingresar_tarea.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\"><br/></span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ingresar_tarea.setPlaceholderText(QCoreApplication.translate("Form", u"Agregar nueva tarea", None))
        self.boton_eliminar_tarea.setText(QCoreApplication.translate("Form", u"Eliminar", None))
        self.boton_agregar_tarea.setText(QCoreApplication.translate("Form", u"Agregar tarea", None))
        self.boton_completar_tarea.setText(QCoreApplication.translate("Form", u"Marcar como completada", None))
    # retranslateUi

