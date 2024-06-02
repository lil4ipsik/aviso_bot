import time

from business import logtime


class WebBot:
    def __init__(self, ui, log_box, driver, login, password):
        self.total_earned_money = 0
        self.ui = ui
        self.log_box = log_box
        self.driver = driver
        self.login = login
        self.password = password
        self.is_paused = False

    def append_log(self, text):
        self.log_box.append(text)
        self.log_box.verticalScrollBar().setValue(self.log_box.verticalScrollBar().maximum())

    def pause(self):
        self.is_paused = True
        self.append_log(f'<font color="yellow">{logtime()} Bot paused</font>')

    def resume(self):
        self.is_paused = False
        self.append_log(f'<font color="yellow">{logtime()} Bot resumed</font>')

    def wait_while_paused(self):
        while self.is_paused:
            time.sleep(0.1)
