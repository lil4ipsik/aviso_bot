import sys

from PySide6.QtWidgets import QApplication

from windows.main_window import MainWindow

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(True)
widget = MainWindow()


def main():
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
