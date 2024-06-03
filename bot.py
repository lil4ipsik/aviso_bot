import random
from pickle import dump as pdump

from aviso import Aviso
from browser import Firefox, Chrome
from profitcentr import Profitcentr
from datetime import datetime
import time
import os
from userdata import *


class Bot:
    def __init__(self, exit_event, ui):
        self.driver = None
        self.is_running = True
        self.ui = ui
        self.login = None
        self.aviso = Aviso(exit_event, ui, ui.log_box)
        self.profitcentr = Profitcentr(exit_event, ui, ui.log_box)
        self.current_bot = self.aviso

        self.bot_dict = {
            'Aviso': self.aviso,
            'Profitcentr': self.profitcentr
        }

    def logtime(self):
        return f'[{datetime.now().replace(microsecond=0)}]'

    def append_log(self, text):
        self.ui.log_box.append(text)

    def run_bot(self, login, password, browser, site):
        self.login = login
        if self.ui.web_site_combo.currentIndex() == -1:
            self.append_log(f'<font color="orange">{self.logtime()} Choice web site</font>')
            return
        self.current_bot = self.bot_dict[site]
        while self.is_running:
            self.append_log(f'<font color="green">{self.logtime()} Using {browser}</font>')
            if browser == 'Firefox':
                self.driver = Firefox().open_browser()
            elif browser == 'Chrome':
                self.driver = Chrome().open_browser()
            self._login(login, password)
            try:
                self.earn_on_bot()
            except Exception as e:
                self.append_log(f'<font color="red">{self.logtime()} {e}</font>')
                continue

        # print('finish run_bot')
        self.append_log(f'<font color="red">{self.logtime()} Bot stopped</font>')
        self.is_running = True

    def earn_on_bot(self):
        is_video_tasks_available = True
        is_website_tasks_available = True
        while self.is_running and self.driver:
            try:
                if is_website_tasks_available or is_video_tasks_available:
                    is_video_tasks_available = self.current_bot.watch_videos(self.driver)
                    for i in range(random.randint(15, 90))[::-1]:
                        if self.is_running:
                            self.append_log(f'<font color="orange">Waiting for {i}seconds</font>')
                            time.sleep(1)
                        else:
                            break
                    is_website_tasks_available = self.current_bot.view_websites(self.driver)
                    for i in range(random.randint(500, 1500))[::-1]:
                        if self.is_running:
                            self.append_log(f'<font color="orange">Waiting for {i}seconds</font>')
                            time.sleep(1)
                        else:
                            break
                    continue
            except Exception as e:
                self.append_log(f'<font color="red">{self.logtime()} {e}</font>')
                for i in range(random.randint(60, 300))[::-1]:
                    if self.is_running:
                        self.append_log(f'<font color="orange">Waiting for {i}seconds</font>')
                        time.sleep(1)
                    else:
                        break
                continue

            self.append_log(f'<font color="red">{self.logtime()} Task isn`t available</font>')
            return

    def get_balance(self):
        return self.aviso.get_balance() + self.profitcentr.get_balance()
    
    def dump_cookies(self):
    # Determine the user's home directory
        self.file_path = path_to_cookies(self)
        print(self.file_path)
        pdump(self.driver.get_cookies(),
            open(self.file_path, "wb"))

    def stop(self):
        self.dump_cookies()
        self.is_running = False
        self.driver.quit()

    def _login(self, login, password):
        try:
            self.current_bot.log_in(self.driver, login, password)
        except Exception as e:
            self.append_log(f'<font color="red">{self.logtime()} {e}</font>')
            self.stop()
