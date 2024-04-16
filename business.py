import datetime
import time

from selenium.common import WebDriverException

from aviso import Aviso
from browser import Firefox, Chrome


class Bot:
    def __init__(self, exit_event, ui):
        self.driver = None
        self.is_running = True
        self.ui = ui
        self.aviso = Aviso(exit_event, ui, ui.log_box)

    def append_log(self, text):
        self.ui.log_box.append(text)
        self.ui.log_box.verticalScrollBar().setValue(self.ui.log_box.verticalScrollBar().maximum())

    def run_bot(self, login, password, browser):
        self.is_running = True
        self.append_log(f'<font color="green">{datetime.datetime.now()} using {browser}</font>')
        if browser == 'Firefox':
            self.driver = Firefox().open_browser()
        elif browser == 'Chrome':
            self.driver = Chrome().open_browser()
        self._login(login, password)
        is_video_tasks_available = True
        is_website_tasks_available = True
        while self.is_running and self.driver:
            try:
                if is_website_tasks_available or is_video_tasks_available:
                    is_video_tasks_available = self.aviso.watch_videos(self.driver)
                    is_website_tasks_available = self.aviso.view_websites(self.driver)
                    continue
            except Exception as e:
                self.append_log(f'<font color="red">{datetime.datetime.now()} {e}</font>')
                continue

            self.append_log(f'<font color="red">{datetime.datetime.now()} task isn`t available</font>')
            for i in range(3000)[::-1]:
                if self.is_running:
                    self.append_log(f'<font color="orange">sleep {i}</font>')
                    time.sleep(1)
                else:
                    break
            is_video_tasks_available = True
            is_website_tasks_available = True
        print('finish run_bot')
        self.append_log(f'<font color="red">{datetime.datetime.now()} bot is stopped</font>')
        self.is_running = True

    def get_balance(self):
        return self.aviso.get_balance()

    def stop(self):
        self.is_running = False
        self.driver.quit()

    def _login(self, login, password):
        try:
            self.aviso.log_in(self.driver, login, password)
        except Exception as e:
            self.append_log(f'<font color="red">{datetime.datetime.now()} {e}</font>')
            self.stop()
