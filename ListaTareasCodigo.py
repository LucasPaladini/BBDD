from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QLineEdit, QMessageBox
from PySide6.QtCore import QStringListModel
from ListaTareas import Ui_Form


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Lista de Tareas")
        self.conectar_botones()  ## Llamar para q funque
        self.modelo = QStringListModel(self)
        self.ui.lista_pantalla.setModel(self.modelo)

    def conectar_botones(self):
        self.ui.boton_agregar_tarea.clicked.connect(lambda: self.agregar_tarea(self.ui.ingresar_tarea))
        self.ui.boton_eliminar_tarea.clicked.connect(self.eliminar_tarea)
        # self.ui.boton_eliminar_tarea.clicked.connect(self.editar_tarea)

    def agregar_tarea(self, texto):
        texto = self.ui.ingresar_tarea.text()
        if texto != "":
            lista_actual = self.modelo.stringList()
            lista_actual.append(texto)
            self.modelo.setStringList(lista_actual)
            self.ui.ingresar_tarea.clear()
        else:
            QMessageBox.warning(self, "Error404", "El campo de texto está vacío")

    def eliminar_tarea(self):
        seleccion = self.ui.lista_pantalla.currentIndex()
        if seleccion.isValid():
            lista_actual = self.modelo.stringList()
            lista_actual.pop(seleccion.row())
            self.modelo.setStringList(lista_actual)
        else:
            QMessageBox.warning(self, "Error 404", "Primero selecciona la tarea.")

    # def completar_tarea(self, texto):
    #     seleccion = self.ui.lista_pantalla.currentIndex()
    #     if seleccion.isValid():
    #         lista_actual = self.modelo.stringList()
    #         lista_actual.
    #         self.modelo.setStringList(lista_actual)



    def iniciar(self):
        self.show()


app = QApplication([])
ventana = Ventana()
ventana.iniciar()
app.exec()
