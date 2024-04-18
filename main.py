########################################################################################
#      Nuitka Configuration (DO NOT CHANGE IF YOU DON'T KNOW WHAT YOU ARE DOING)       
#                                                                                      
# nuitka-project: --onefile --include-data-files=windows/icon.ico=windows/icon.ico     
# nuitla-project: --deployment --disable-console --enable-plugin=pyside6               
# nuitka-project: --output-dir=build --product-name="Aviso Bot"                        
# nuitka-project: --windows-icon-from-ico=windows/icon.ico --product-version=0.0.0.4   
# nuitka-project: -o "aviso bot"                                                       
########################################################################################

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
