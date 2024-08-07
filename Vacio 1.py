from PySide6.QtWidgets import QApplication, QLabel, QWidget
import sys

# Crea una aplicación Qt
app = QApplication(sys.argv)

# Crea un widget
window = QWidget()
window.setWindowTitle('Prueba de PySide6')
window.setGeometry(100, 100, 800, 500)  # x, y, ancho, alto

# Agrega una etiqueta
label = QLabel('¡Hola, PySide6!', window)
label.setGeometry(100, 80, 100, 300)  # x, y, ancho, alto

# Muestra el widget
window.show()

# Ejecuta el ciclo de eventos
sys.exit(app.exec())