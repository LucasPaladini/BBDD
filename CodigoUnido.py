import sys
from PySide6.QtWidgets import QApplication, QWidget
from QTDesigner_ui_cod import Ui_Form

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupConnections()

    def setupConnections(self):
        # Conecta el botón 1 a la función handleButton1
        self.pushButton.setText("1")
        self.pushButton.clicked.connect(self.handleButton1)

    def handleButton1(self):
        current_text = self.textEdit.toPlainText()
        new_text = current_text + "1"
        self.textEdit.setPlainText(new_text)

#asd

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
