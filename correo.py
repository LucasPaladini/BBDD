from PySide6 import QtWidgets, QtCore
from nuevo_correoo import Ui_Correo

class Cartero:
    def entregar(self, mensaje):
        print(f"Se envió: {mensaje}")

class ControladorDeEnvioDeCorreo:
    def __init__(self):
        self.__ventana = VentanaNuevoMensaje()
        self.__cartero = Cartero()
        self.__ventana.mensaje_confirmado.connect(self.enviar_correo)

    def iniciar(self):
        self.__ventana.show()

    @QtCore.Slot(dict)
    def enviar_correo(self, correo):
        self.__cartero.entregar(correo["mensaje"])

class VentanaNuevoMensaje(QtWidgets.QWidget):
    mensaje_confirmado = QtCore.Signal(dict)

    def __init__(self):
        super().__init__()
        self.__ui = Ui_Correo()
        self.__ui.setupUi(self)
        self.__setupgui()
        self.toggle_button()  # Asegúrate de que el botón esté deshabilitado al inicio

    def __setupgui(self):
        self.__ui.plainTextEdit_mensaje.textChanged.connect(self.toggle_button)
        self.__ui.enviar.clicked.connect(self.enviar_correo)  # Conectar el botón "Enviar"

    def toggle_button(self):
        # Habilitar o deshabilitar el botón según si hay texto
        self.__ui.enviar.setDisabled(self.__ui.plainTextEdit_mensaje.toPlainText().strip() == "")

    def enviar_correo(self):
        self.mensaje_confirmado.emit({"mensaje": self.__ui.plainTextEdit_mensaje.toPlainText()})

app = QtWidgets.QApplication([])

controlador = ControladorDeEnvioDeCorreo()
controlador.iniciar()

app.exec()
