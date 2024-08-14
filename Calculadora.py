import sys
from PySide6.QtWidgets import (QApplication, QWidget, QTextEdit, QPushButton, QGridLayout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Calculadora')
        self.generar_interfaz()
        self.show()

<<<<<<< HEAD
    def generar_interfaz(self):
        self.pantalla = QTextEdit()
        self.pantalla.setDisabled(True)
=======
    # QPushButton
    # background-color
    #
    # QPushButton:pressed (
    #     background-color: #e89127
    # )
    def generar_interfaz(self):
        self.pantalla = QTextEdit()
        self.pantalla.setDisabled(False)
>>>>>>> fcc640a (Calculadora funcionando)
        boton_1 = QPushButton("1")
        boton_2 = QPushButton("2")
        boton_3 = QPushButton("3")
        boton_4 = QPushButton("4")
        boton_5 = QPushButton("5")
        boton_6 = QPushButton("6")
        boton_7 = QPushButton("7")
        boton_8 = QPushButton("8")
        boton_9 = QPushButton("9")
        boton_0 = QPushButton("0")
<<<<<<< HEAD
        boton_punto = QPushButton(".")
=======
        boton_coma = QPushButton(",")
>>>>>>> fcc640a (Calculadora funcionando)

        boton_suma = QPushButton("+")
        boton_resta = QPushButton("-")
        boton_multiplicacion = QPushButton("*")
        boton_division = QPushButton("/")
<<<<<<< HEAD

        boton_ce = QPushButton("CE")
        boton_borrar = QPushButton("<-")
=======
        boton_division.setStyleSheet("background-color: #e89127")

        boton_AC = QPushButton("AC")
        boton_mas_menos = QPushButton("+/-")
        boton_porciento = QPushButton("%")
>>>>>>> fcc640a (Calculadora funcionando)
        boton_resultado = QPushButton("=")

        self.main_grid = QGridLayout()
        self.main_grid.addWidget(self.pantalla, 0, 0, 2, 4)
<<<<<<< HEAD
        self.main_grid.addWidget(boton_ce, 2, 0, 1, 2)
        self.main_grid.addWidget(boton_borrar, 2, 2)
        self.main_grid.addWidget(boton_suma, 2, 3)
=======
        self.main_grid.addWidget(boton_AC, 2, 0, 1, 1)
        self.main_grid.addWidget(boton_mas_menos, 2, 1, 1, 1)
        self.main_grid.addWidget(boton_porciento, 2, 2)
        self.main_grid.addWidget(boton_division, 2, 3)
>>>>>>> fcc640a (Calculadora funcionando)

        self.main_grid.addWidget(boton_7, 3, 0)
        self.main_grid.addWidget(boton_8, 3, 1)
        self.main_grid.addWidget(boton_9, 3, 2)
<<<<<<< HEAD
        self.main_grid.addWidget(boton_division, 3, 3)
=======
        self.main_grid.addWidget(boton_multiplicacion, 3, 3)
>>>>>>> fcc640a (Calculadora funcionando)

        self.main_grid.addWidget(boton_4, 4, 0)
        self.main_grid.addWidget(boton_5, 4, 1,)
        self.main_grid.addWidget(boton_6, 4, 2,)
<<<<<<< HEAD
        self.main_grid.addWidget(boton_multiplicacion, 4, 3,)
=======
        self.main_grid.addWidget(boton_resta, 4, 3,)
>>>>>>> fcc640a (Calculadora funcionando)

        self.main_grid.addWidget(boton_1, 5, 0,)
        self.main_grid.addWidget(boton_2, 5, 1,)
        self.main_grid.addWidget(boton_3, 5, 2,)
<<<<<<< HEAD
        self.main_grid.addWidget(boton_resta, 5, 3,)

        self.main_grid.addWidget(boton_0, 6, 0,)
        self.main_grid.addWidget(boton_punto, 6, 2,)
=======
        self.main_grid.addWidget(boton_suma, 5, 3,)

        self.main_grid.addWidget(boton_0, 6, 0, 1, 2)
        self.main_grid.addWidget(boton_coma, 6, 2,)
>>>>>>> fcc640a (Calculadora funcionando)
        self.main_grid.addWidget(boton_resultado, 6, 3,)

        self.setLayout(self.main_grid)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
<<<<<<< HEAD
    sys.exit(app.exec_())
=======
    sys.exit(app.exec_())
>>>>>>> fcc640a (Calculadora funcionando)
