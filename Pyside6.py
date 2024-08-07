# from PySide6.QtWidgets import QApplication, QLabel, QWidget
# import sys
#
# # Crea una aplicación Qt
# app = QApplication(sys.argv)
#
# # Crea un widget
# window = QWidget()
# window.setWindowTitle('Prueba de PySide6')
# window.setGeometry(100, 100, 800, 500)  # x, y, ancho, alto
#
# # Agrega una etiqueta
# label = QLabel('¡Hola, PySide6!', window)
# label.setGeometry(100, 80, 100, 300)  # x, y, ancho, alto
#
# # Muestra el widget
# window.show()
#
# # Ejecuta el ciclo de eventos
# sys.exit(app.exec())


import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel

class VentanaVacia(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Opaaa')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaVacia()
    sys.exit(app.exec_())

#a
