########################################################################################
#      Nuitka Configuration (DO NOT CHANGE IF YOU DON'T KNOW WHAT YOU ARE DOING)       
#                                                                                     
# nuitka-project: --include-data-files={MAIN_DIRECTORY}/windows/icon.ico=windows/icon.ico
# nuitka-project: --include-data-files={MAIN_DIRECTORY}/res/version.json=res/version.json   
# nuitka-project: --deployment
# nuitka-project: --disable-console
# nuitka-project: --enable-plugin=pyside6               
# nuitka-project: --output-dir={MAIN_DIRECTORY}/build
# nuitka-project: --product-name="Aviso Bot"                        
# nuitka-project: --windows-icon-from-ico={MAIN_DIRECTORY}/windows/icon.ico
# nuitka-project: --product-version=0.0.0.6   
# nuitka-project: -o "aviso-bot"                                                    
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
