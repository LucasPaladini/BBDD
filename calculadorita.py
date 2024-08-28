
from PySide6 import QtWidgets
from calculadora import Ui_Form

class Calculadora(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Calculadora")
        
        self.ui.boton1.clicked.connect(lambda: self.__agregar_a_resultado("1"))
        self.ui.boton2.clicked.connect(lambda: self.__agregar_a_resultado("2"))
        self.ui.boton3.clicked.connect(lambda: self.__agregar_a_resultado("3"))
        self.ui.boton4.clicked.connect(lambda: self.__agregar_a_resultado("4"))
        self.ui.boton5.clicked.connect(lambda: self.__agregar_a_resultado("5"))
        self.ui.boton6.clicked.connect(lambda: self.__agregar_a_resultado("6"))
        self.ui.boton7.clicked.connect(lambda: self.__agregar_a_resultado("7"))
        self.ui.boton8.clicked.connect(lambda: self.__agregar_a_resultado("8"))
        self.ui.boton9.clicked.connect(lambda: self.__agregar_a_resultado("9"))
        self.ui.boton0.clicked.connect(lambda: self.__agregar_a_resultado("0"))
        self.ui.boton_suma.clicked.connect(lambda: self.__agregar_a_resultado("+"))
        self.ui.boton_resta.clicked.connect(lambda: self.__agregar_a_resultado("-"))
        self.ui.boton_multiplicacion.clicked.connect(lambda: self.__agregar_a_resultado("*"))
        self.ui.boton_division.clicked.connect(lambda: self.__agregar_a_resultado("/"))
        self.ui.boton_resultado.clicked.connect(self.__calcular_resultado)
        self.ui.boton_borrar.clicked.connect(self.__borrar)

    def __agregar_a_resultado(self, texto):
        self.ui.layout_resultado.setText(self.ui.layout_resultado.text() + texto)

    def __agregar_a_resultado_1(self):
        self.__agregar_a_resultado("1")

    def __agregar_a_resultado_1(self):
        self.__agregar_a_resultado("1")
    def __agregar_a_resultado_1(self):
        self.__agregar_a_resultado("1")

    def __agregar_a_resultado_1(self):
        self.__agregar_a_resultado("1")

    def __agregar_a_resultado_1(self):
        self.__agregar_a_resultado("1")

    def __agregar_a_resultado_1(self):
        self.__agregar_a_resultado("1")

    def __agregar_a_resultado_1(self):
        self.__agregar_a_resultado("1")

    def __agregar_a_resultado_1(self):
        self.__agregar_a_resultado("1")

    def __agregar_a_resultado_1(self):
        self.__agregar_a_resultado("1")

    def __agregar_a_resultado_1(self):
        self.__agregar_a_resultado("1")

    def __calcular_resultado(self):
        resultado = eval(self.ui.layout_resultado.text())
        self.ui.layout_resultado.setText(str(resultado))


    def __borrar(self):
        self.ui.layout_resultado.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    calculadora = Calculadora()
    calculadora.show()
    app.exec()
