import time

from aviso import Aviso


class Bot:
    def __init__(self, exit_event):
        self.driver = None
        self.aviso = Aviso(exit_event)

    def run_bot(self):
        self.driver = self.aviso.log_in()
        #  print(f'{datetime.datetime.now()} {strings["sleep"][lan]} 5 {strings["seconds"][lan]}')
        time.sleep(5)
        is_video_tasks_available = True
        is_website_tasks_available = True
        while True and self.driver:
            try:
                if is_website_tasks_available or is_video_tasks_available:
                    is_video_tasks_available = self.aviso.watch_videos(self.driver)
                    is_website_tasks_available = self.aviso.view_websites(self.driver)
                else:
                    #  print(f'{datetime.datetime.now()} {strings["tasks_is_not_available"][lan]}')
                    #  print(f'{datetime.datetime.now()} {strings["sleep"][lan]} 3600 {strings["seconds"][lan]}')
                    for i in range(3600)[::-1]:
                        #  print(f'{bcolors.WARNING}sleep {i}s')
                        time.sleep(1)
                    is_video_tasks_available = True
                    is_website_tasks_available = True
            except Exception as e:
                # print(f'{bcolors.FAIL}{e}{bcolors.ENDC}')
                #  print(f'{datetime.datetime.now()} {strings["sleep"][lan]} 60 {strings["seconds"][lan]}')
                continue

    def get_balance(self):
        return self.aviso.get_balance()

    def stop(self):
        self.driver.quit()
        self.driver = None
