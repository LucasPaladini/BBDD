# from PySide6 import QtWidgets, QtCore, QtGui
# from PySide6.QtWidgets import QApplication
#
# class FrutasModel(QtCore.QAbstractListModel):
#     def __init__(self):
#         super().__init__()
#         self.autos = ["siena", "CORSA", "hilux", "vEcTrA"]
#
#     def rowCount(self, parent=None):
#         return len(self.autos)
#
#     def flags(self, index):
#         return QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsEditable
#
#     def setData(self, index, value, role=QtCore.Qt.ItemDataRole.EditRole):
#         if index.isValid() and role == QtCore.Qt.ItemDataRole.EditRole:
#             self.autos[index.row()] = value
#             self.dataChanged.emit(index, index, [role])
#             return True
#         return False
#
#     def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
#         if index.isValid():
#             if role == QtCore.Qt.ItemDataRole.DisplayRole:
#                 return self.autos[index.row()].capitalize()
#             if role == QtCore.Qt.ItemDataRole.EditRole:
#                 return self.autos[index.row()].upper()
#             if role == QtCore.Qt.ItemDataRole.ForegroundRole:
#                 row = index.row() + 1
#                 if row % 2 == 0:
#                     return QtGui.QColor(255, 0, 0)
#             if role == QtCore.Qt.ItemDataRole.BackgroundRole:
#                 return QtGui.QColor(200, 200, 200)
#             if role == QtCore.Qt.ItemDataRole.FontRole:
#                 font = QtGui.QFont()
#                 font.setBold(True)
#                 return font
#         return None
#
#
# if __name__ == "__main__":
#     app = QApplication([])
#
#     # Crear lista y configurar el modelo
#     lista = QtWidgets.QListView()
#     lista.setModel(FrutasModel())
#
#     # Hacer QMainWindow y centrarlo
#     main_window = QtWidgets.QMainWindow()
#     main_window.setCentralWidget(lista)
#
#     main_window.setWindowTitle("Autos alta gama")
#
#     main_window.show()
#
#     app.exec()



# Dos columnas

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QApplication


class Autos_color(QtCore.QAbstractTableModel):
    def __init__(self):
        super().__init__()
        # Lista nombre y tipo
        self.autos = [
            ["siena", "verde"],
            ["corsa", "negro"],
            ["hilux", "gris"],
            ["vectra", "azul"]]

    def rowCount(self, parent=None):
        return len(self.autos)

    def columnCount(self, parent=None):
        return 2  # Dos columnas: nombre y tipo

    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if index.isValid():
            row = index.row()
            column = index.column()
            if role == QtCore.Qt.ItemDataRole.DisplayRole:
                return self.autos[row][column].capitalize()
            if role == QtCore.Qt.ItemDataRole.EditRole:
                return self.autos[row][column]
            if role == QtCore.Qt.ItemDataRole.FontRole:
                font = QtGui.QFont()
                font.setBold(True)
                return font
        return None

    def setData(self, index, value, role=QtCore.Qt.ItemDataRole.EditRole):
        if index.isValid() and role == QtCore.Qt.ItemDataRole.EditRole:
            row = index.row()
            column = index.column()
            self.autos[row][column] = value
            self.dataChanged.emit(index, index, [role])
            return True
        return False

    def headerData(self, section, orientation, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                if section == 0:
                    return "Nombre"
                elif section == 1:
                    return "Tipo"
        return None


if __name__ == "__main__":
    app = QApplication([])

    # Crear vista de tabla y modelo
    tabla = QtWidgets.QTableView()
    tabla.setModel(Autos_color())

    # Crear QMainWindow y centrar widget
    main_window = QtWidgets.QMainWindow()
    main_window.setCentralWidget(tabla)

    # Título
    main_window.setWindowTitle("Colores de autos")

    # Ver ventana principal
    main_window.show()
    app.exec()
