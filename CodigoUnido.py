from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QLineEdit
from QTDesigner_ui_codigo import Ui_Form


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Calculadora ISPI 4038")

    def conector_botones_pantalla(self):
        # Conectar msj de botones al mostrar
        self.ui.boton_ac.clicked.connect(lambda: self.__agregar_valor("AC"))
        self.ui.boton_cambio_signo.clicked.connect(lambda: self.__agregar_valor("+/-"))
        self.ui.boton_porciento.clicked.connect(lambda: self.__agregar_valor("%"))
        self.ui.boton_dividido.clicked.connect(lambda: self.__agregar_valor("/"))
        self.ui.boton_multiplicacion.clicked.connect(lambda: self.__agregar_valor("*"))
        self.ui.boton_suma.clicked.connect(lambda: self.__agregar_valor("+"))
        self.ui.boton_menos.clicked.connect(lambda: self.__agregar_valor("-"))
        self.ui.boton_igual.clicked.connect(lambda: self.__agregar_valor("="))
        self.ui.boton_coma.clicked.connect(lambda: self.__agregar_valor(","))
        self.ui.boton_1.clicked.connect(lambda: self.__agregar_valor("1"))
        self.ui.boton_2.clicked.connect(lambda: self.__agregar_valor("2"))
        self.ui.boton_3.clicked.connect(lambda: self.__agregar_valor("3"))
        self.ui.boton_4.clicked.connect(lambda: self.__agregar_valor("4"))
        self.ui.boton_5.clicked.connect(lambda: self.__agregar_valor("5"))
        self.ui.boton_6.clicked.connect(lambda: self.__agregar_valor("6"))
        self.ui.boton_7.clicked.connect(lambda: self.__agregar_valor("7"))
        self.ui.boton_8.clicked.connect(lambda: self.__agregar_valor("8"))
        self.ui.boton_9.clicked.connect(lambda: self.__agregar_valor("9"))
        self.ui.boton_0.clicked.connect(lambda: self.__agregar_valor("0"))
        self.ui.boton_igual.clicked.connect(self.__calcular_resultado)
        self.ui.boton_ac.clicked.connect(self.__borrar)

    def __agregar_valor(self, texto):
        self.ui.textEdit.setText(self.ui.textEdit.text() + texto)

    def __calcular_resultado(self):
        resultado = eval(self.ui.textEdit.text())
        self.ui.textEdit.setText(str(resultado))

    def __borrar(self):
        self.ui.textEdit.clear()


    # @Slot()
    # def on_pushButton_clicked(self):
    #     print("Hola")

    def iniciar(self):
        self.show()


app = QApplication([])
main_window = MainWindow()
main_window.iniciar()

app.exec()
