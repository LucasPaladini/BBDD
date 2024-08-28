from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QLineEdit
from PySide6.QtCore import Slot
from QTDesigner_ui_cod import Ui_Form  # Asegúrate de que este nombre coincida con el archivo que contiene Ui_Form

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__setup_connections()

    def mostrar(self, texto):
        self.ui.setText(self.ui.text() + texto)

    def resultado(self):
        resultado = eval(self.pantalla.text())
        self.pantalla.setText(str(resultado))

    def __setup_connections(self):
        # Conectar señales de botones a métodos
        self.ui.pushButton.clicked.connect(lambda: self.mostrar("AC"), pantalla.clear())
        self.ui.pushButton_2.clicked.connect(lambda: self.mostrar("+/-"))
        self.ui.pushButton_3.clicked.connect(lambda: self.mostrar("%"))
        self.ui.pushButton_4.clicked.connect(lambda: self.mostrar("/"))
        self.ui.pushButton_5.clicked.connect(lambda: self.mostrar("*"))
        self.ui.pushButton_6.clicked.connect(lambda: self.mostrar("7"))
        self.ui.pushButton_7.clicked.connect(lambda: self.mostrar("8"))
        self.ui.pushButton_8.clicked.connect(lambda: self.mostrar("9"))
        self.ui.pushButton_9.clicked.connect(lambda: self.mostrar("-"))
        self.ui.pushButton_10.clicked.connect(lambda: self.mostrar("1"))
        self.ui.pushButton_11.clicked.connect(lambda: self.mostrar("4"))
        self.ui.pushButton_12.clicked.connect(lambda: self.mostrar("3"))
        self.ui.pushButton_13.clicked.connect(lambda: self.mostrar("5"))
        self.ui.pushButton_14.clicked.connect(lambda: self.mostrar("+"))
        self.ui.pushButton_15.clicked.connect(lambda: self.mostrar("6"))
        self.ui.pushButton_16.clicked.connect(lambda: self.mostrar("2"))
        self.ui.pushButton_17.clicked.connect(lambda: self.mostrar("0"))
        self.ui.pushButton_18.clicked.connect(lambda: self.mostrar("="))
        self.ui.pushButton_19.clicked.connect(lambda: self.mostrar(","))


    @Slot()
    def on_pushButton_clicked(self):
        print("Hola")

    def iniciar(self):
        self.show()


app = QApplication([])
main_window = MainWindow()
main_window.iniciar()

app.exec()
