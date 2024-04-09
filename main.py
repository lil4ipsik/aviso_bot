import threading
import datetime
import time

from selenium.common.exceptions import TimeoutException, NoSuchWindowException

from res.string import strings
from settings import Settings
from aviso import Aviso


_settings = Settings()
settings = _settings.get_settings()
lan = settings['language']
exit_event = threading.Event()


def start_config(_exit_event):
    global _settings
    global lan
    aviso = Aviso(_settings, _exit_event)
    driver = aviso.log_in()
    print(f'{datetime.datetime.now()} {strings["sleep"][lan]} 5 {strings["seconds"][lan]}')
    time.sleep(5)
    is_video_tasks_available = True
    is_website_tasks_available = True
    while True:
        try:
            if is_website_tasks_available or is_video_tasks_available:
                is_video_tasks_available = aviso.watch_videos(driver)['is_tasks_available']
                is_website_tasks_available = aviso.view_websites(driver)['is_tasks_available']
            else:
                print(f'{datetime.datetime.now()} {strings["tasks_is_not_available"][lan]}')
                exit_event.set()
                print(f'{datetime.datetime.now()} {strings["bot_paused"][lan]}')
                is_video_tasks_available = True
                is_website_tasks_available = True
        except (TimeoutException, NoSuchWindowException):
            print(f'{datetime.datetime.now()} {strings["sleep"][lan]} 60 {strings["seconds"][lan]}')
            time.sleep(60)
            continue


def main():
    thread = threading.Thread(target=start_config, args=(exit_event,))
    thread.start()
    try:
        while True:
            command = input(f'\n{strings["command_list"][lan]}\n')
            if command == "pause":
                exit_event.set()
                print(f'{datetime.datetime.now()} {strings["bot_paused"][lan]}')
            elif command == "resume":
                exit_event.clear()
                print(f'{datetime.datetime.now()} {strings["bot_resume"][lan]}')
            elif command == "stop":
                quit()
            else:
                print(f'{strings["invalid_command"][lan]} {strings["command_list"][lan]}\n')
    except Exception as e:
        print(e)

    thread.join()


if __name__ == "__main__":
    main()