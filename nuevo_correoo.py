from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Correo(object):
    def setupUi(self, Correo):
        if not Correo.objectName():
            Correo.setObjectName(u"Correo")
        Correo.resize(400, 400)
        Correo.setMinimumSize(QSize(400, 400))
        Correo.setMaximumSize(QSize(400, 400))
        self.gridLayout = QGridLayout(Correo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 1, 1, 1)

        self.label_mensaje = QLabel(Correo)
        self.label_mensaje.setObjectName(u"label_mensaje")

        self.gridLayout.addWidget(self.label_mensaje, 3, 0, 1, 1)

        self.enviar = QPushButton(Correo)
        self.enviar.setObjectName(u"enviar")
        self.enviar.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.enviar, 5, 2, 1, 1)

        self.plainTextEdit_mensaje = QPlainTextEdit(Correo)
        self.plainTextEdit_mensaje.setObjectName(u"plainTextEdit_mensaje")

        self.gridLayout.addWidget(self.plainTextEdit_mensaje, 4, 0, 1, 3)


        self.retranslateUi(Correo)

        QMetaObject.connectSlotsByName(Correo)
    # setupUi

    def retranslateUi(self, Correo):
        Correo.setWindowTitle(QCoreApplication.translate("Correo", u"Correo", None))
        self.label_mensaje.setText(QCoreApplication.translate("Correo", u"Mensaje:", None))
        self.enviar.setText(QCoreApplication.translate("Correo", u"Enviar", None))
    # retranslateUi
