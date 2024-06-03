import random
from pickle import dump as pdump
from PyQt6.QtCore import QThread

from aviso import Aviso
from browser import Firefox, Chrome
from business import logtime
from profitcentr import Profitcentr
import time


class Bot(QThread):
    def __init__(self, ui, login, password):
        super().__init__()
        self.driver = None
        self.is_running = True
        self.ui = ui
        self.login = login
        self.password = password
        self.current_bot = None

    def append_log(self, text):
        self.ui.log_box.append(text)

    def run(self):
        if self.ui.web_site_combo.currentIndex() == -1:
            self.append_log(f'<font color="orange">{logtime()} Choice web site</font>')
            return
        self.append_log(f'<font color="green">{logtime()} Using {self.ui.comboBox.currentText()}</font>')
        try:
            if self.ui.comboBox.currentText() == 'Firefox':
                self.driver = Firefox().open_browser()
            elif self.ui.comboBox.currentText() == 'Chrome':
                self.driver = Chrome().open_browser()

            if self.ui.web_site_combo.currentText() == 'Aviso':
                self.current_bot = Aviso(self.ui, self.ui.log_box, self.driver, self.login,
                                         self.password)
            else:
                self.current_bot = Profitcentr(self.ui, self.ui.log_box, self.driver, self.login,
                                               self.password)
            self._login()
        except Exception as e:
            self.append_log(f'<font color="red">{logtime()} {e}</font>')
            return
        while self.is_running:
            try:
                self.earn_on_bot()
            except Exception as e:
                self.append_log(f'<font color="red">{logtime()} {e}</font>')
                continue

        self.append_log(f'<font color="red">{logtime()} Bot stopped</font>')
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
                self.append_log(f'<font color="red">{logtime()} {e}</font>')
                for i in range(random.randint(60, 300))[::-1]:
                    if self.is_running:
                        self.append_log(f'<font color="orange">Waiting for {i}seconds</font>')
                        time.sleep(1)
                    else:
                        break
                continue

            self.append_log(f'<font color="red">{logtime()} Task isn`t available</font>')
            return

    def get_balance(self):
        return self.current_bot.get_balance() if self.current_bot else 0

    def stop(self):
        if self.login:
            pdump(self.driver.get_cookies(),
                  open(f"{self.ui.web_site_combo.currentText().lower()}_{self.login}_cookies", "wb"))
        self.is_running = False
        self.driver.quit()
        self.terminate()

    def pause(self):
        if self.current_bot:
            self.current_bot.pause()

    def resume(self):
        if self.current_bot:
            self.current_bot.resume()

    def _login(self):
        try:
            self.current_bot.log_in()
        except Exception as e:
            self.append_log(f'<font color="red">{logtime()} {e}</font>')
            self.stop()
