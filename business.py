from datetime import datetime
from time import sleep

from selenium.common import WebDriverException

from aviso import Aviso
from browser import Firefox, Chrome


class Bot:
    def __init__(self, exit_event, ui):
        self.driver = None
        self.is_running = True
        self.ui = ui
        self.aviso = Aviso(exit_event, ui, ui.log_box)

    def logtime(self):
        return f'[{datetime.now().replace(microsecond=0)}]'

    def append_log(self, text):
        self.ui.log_box.append(text)

    def run_bot(self, login, password, browser):
        self.is_running = True
        self.append_log(f'<font color="green">{self.logtime()} Using {browser}</font>')
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
                self.append_log(f'<font color="red">{self.logtime()} {e}</font>')
                continue

            self.append_log(f'<font color="red">{self.logtime()} Task isn`t available</font>')
            for i in range(3000)[::-1]:
                if self.is_running:
                    self.append_log(f'<font color="orange">Waiting for {i}seconds</font>')
                    sleep(1)
                else:
                    break
            is_video_tasks_available = True
            is_website_tasks_available = True
        # print('finish run_bot')
        self.append_log(f'<font color="red">{self.logtime()} Bot stopped</font>')
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
            self.append_log(f'<font color="red">{self.logtime()} {e}</font>')
            self.stop()
