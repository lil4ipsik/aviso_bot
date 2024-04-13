import datetime
import time

from aviso import Aviso


class Bot:
    def __init__(self, exit_event, ui):
        self.driver = None
        self.ui = ui
        self.aviso = Aviso(exit_event, ui.log_box)

    def run_bot(self):
        self.driver = self.aviso.log_in()
        time.sleep(5)
        is_video_tasks_available = True
        is_website_tasks_available = True
        while True and self.driver:
            try:
                if is_website_tasks_available or is_video_tasks_available:
                    is_video_tasks_available = self.aviso.watch_videos(self.driver)
                    is_website_tasks_available = self.aviso.view_websites(self.driver)
                else:
                    self.ui.log_box.append(f'<font color="red">{datetime.datetime.now()} task isn`t available</font>')
                    for i in range(3600)[::-1]:
                        self.ui.log_box.append(f'<font color="orange">sleep {i}</font>')
                        time.sleep(1)
                    is_video_tasks_available = True
                    is_website_tasks_available = True
            except Exception as e:
                self.ui.log_box.append(f'<font color="red">{datetime.datetime.now()} {e}</font>')
                continue

    def get_balance(self):
        return self.aviso.get_balance()

    def stop(self):
        self.driver.quit()
        self.driver = None
