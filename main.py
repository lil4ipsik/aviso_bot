import threading
import time

from colorama import just_fix_windows_console

from aviso import Aviso
from bcolors import bcolors
from settings import Settings
import sys
from PySide6.QtWidgets import QApplication
from windows.main_window import MainWindow


app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(True)
widget = MainWindow()
just_fix_windows_console()
_settings = Settings()
settings = _settings.get_settings()
lan = settings['language']


def main():
    #thread = threading.Thread(target=start_config, args=(exit_event,))
    #thread.start()
    # try:
    #     while True:
    #         command = input(f'\n{bcolors.OKGREEN}{bcolors.ENDC}\n')
    #         if command == "pause":
    #             exit_event.set()
    #             #  print(f'{datetime.datetime.now()} {strings["bot_paused"][lan]}')
    #         elif command == "resume":
    #             exit_event.clear()
    #             #  print(f'{datetime.datetime.now()} {strings["bot_resume"][lan]}')
    #         elif command == "stop":
    #             quit()
    #         else:
    #             print(f'invalid\n')
    # except Exception as e:
    #     print(f"{bcolors.FAIL}{e}{bcolors.ENDC}")

    #thread.join()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
