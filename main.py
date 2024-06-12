import sys

from PyQt6.QtWidgets import QApplication

from windows.main_window import MainWindow

app = QApplication([])
app.setStyle('Fusion')
window = MainWindow()
window.show()
sys.exit(app.exec())
