import time
from datetime import datetime
from pickle import dump as pdump, load as pload
from time import sleep
from os.path import exists

from colorama import just_fix_windows_console
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()
just_fix_windows_console()


def _is_captcha_available(driver):
    if len(driver.find_elements(By.ID, 'out-capcha')) != 0 or len(driver.find_elements(By.CLASS_NAME, 'out-capcha')) != 0:
        return True
    else:
        return False


class Profitcentr:
    def __init__(self, exit_event, ui, log_box):
        self.profitcentr_url = "https://profitcentr.com/"
        self.total_earned_money = 0
        self.exit_event = exit_event
        self.ui = ui
        self.log_box = log_box

    def logtime(self):
        return f'[{datetime.now().replace(microsecond=0)}]'

    def append_log(self, text):
        self.log_box.append(text)
        self.log_box.verticalScrollBar().setValue(self.log_box.verticalScrollBar().maximum())

    def get_balance(self):
        return self.total_earned_money

    def view_websites(self, driver):
        while self.exit_event.is_set():
            sleep(1)
        self.append_log(f'<font color="">{self.logtime()} Surf web</font>')
        if driver.find_element(By.ID, 'mnu_tblock1').value_of_css_property("display") == "none":
            driver.find_element(By.ID, 'mnu_title1').click()
            time.sleep(3)
        driver.find_element(By.ID, 'mnu_tblock1').find_elements(By.TAG_NAME, 'a')[1].click()
        time.sleep(3)
        while self.exit_event.is_set():
            sleep(1)
        while _is_captcha_available(driver):
            self.append_log(f'<font color="red">{self.logtime()} COMPLETE CAPTCHA</font>')
            time.sleep(1)

        # if 'Посещение сайтов' in driver.page_source:
        #     print(f"'Посещение сайтов' in driver.page_source{'Посещение сайтов' in driver.page_source}")
        #     self.log_in(driver, self.ui.login_edit.text(), self.ui.password_edit.text())
        #     return True
        error_count = 0
        website_list = driver.find_elements(By.CLASS_NAME, "work-serf")
        print(website_list)
        is_tasks_available = True
        if len(website_list) > 0 and not ('Нет переходов доступных для просмотра, зайдите немного позже' in
                                          driver.find_element(By.CLASS_NAME, "msg-error").text):
            for i in website_list:
                while self.exit_event.is_set():
                    sleep(1)
                while _is_captcha_available(driver):
                    self.append_log(f'<font color="red">{self.logtime()} COMPLETE CAPTCHA</font>')
                    time.sleep(1)
                if error_count >= 3:
                    return False
                try:
                    a = i.find_element(By.TAG_NAME, "a")
                    price_span = i.find_element(By.XPATH, 'tbody/tr/td[3]/span[2]')
                    time_span = i.find_element(By.XPATH, "tbody/tr/td[2]/div[1]/a")
                    print(price_span.get_attribute('innerHTML').split(' ')[0], time_span.get_attribute('onclick').replace("'", '').split(',')[2])
                    earned_money = float(price_span.get_attribute('innerHTML').split(' ')[0])
                    time_sleep = int(time_span.get_attribute('onclick').replace("'", '').split(',')[2]) + 5
                    a.click()
                    sleep(1.5)
                except Exception as e:
                    self.append_log(f'<font color="red">{self.logtime()} {e}</font>')
                    error_count += 1
                    continue

                for j in range(5):
                    if len(driver.window_handles) < 2:
                        sleep(1)
                        continue
                    else:
                        break

                if len(driver.window_handles) < 2:
                    continue

                try:
                    driver.switch_to.window(driver.window_handles[1])
                    sleep(time_sleep)
                except Exception as e:
                    self.append_log(f'<font color="red">{self.logtime()} {e}</font>')
                    error_count += 1
                    sleep(3)
                else:
                    sleep(0.5)
                    self.total_earned_money += earned_money
                    self.append_log(f'<font color="green">{self.logtime()} Earned: '
                                    f'{round(earned_money, 5)}, total: {round(self.total_earned_money, 5)}</font>')
                for handle in driver.window_handles[1:]:
                    driver.switch_to.window(handle)
                    driver.close()

                driver.switch_to.window(driver.window_handles[0])
                sleep(1)
        else:
            is_tasks_available = False

        return is_tasks_available

    def watch_videos(self, driver):
        while self.exit_event.is_set():
            sleep(1)
        self.append_log(f'<font color="">{self.logtime()} Watch YouTube</font>')

        driver.get("https://aviso.bz/work-youtube")
        while _is_captcha_available(driver):
            self.append_log(f'<font color="red">{self.logtime()} WARNING, COMPLETE THE CAPTCHA</font>')
            sleep(1)
        wait = WebDriverWait(driver, 7)
        error_count = 0
        video_list = []
        if driver.find_elements(By.CLASS_NAME, "form-control"):
            self.log_in(driver, self.ui.login_edit.text(), self.ui.password_edit.text())
        for task in driver.find_elements(By.CLASS_NAME, "work-serf"):
            if 'Просмотр видеоролика' in task.text:
                video_list.append(task)
        is_tasks_available = True if video_list else False
        if len(video_list) > 0:
            for i in video_list:
                while self.exit_event.is_set():
                    sleep(1)
                if error_count >= 3:
                    return False
                try:
                    a = i.find_element(By.TAG_NAME, "span")
                    price_span = i.find_element(By.XPATH, "tbody/tr/td[3]/span[2]")
                    time_span = i.find_element(By.XPATH, "tbody/tr/td[3]/div/span[1]")
                    earned_money = float(price_span.get_attribute('innerHTML').split('<')[0])
                    time_sleep = int(time_span.get_attribute('innerHTML').split()[0]) + 3
                    a.click()
                    sleep(1.5)
                except Exception as e:
                    self.append_log(f'<font color="red">{self.logtime()} {e}</font>')
                    error_count += 1
                    continue

                for j in range(5):
                    if len(driver.window_handles) < 2:
                        sleep(1)
                        continue
                    else:
                        break

                if len(driver.window_handles) < 2:
                    continue

                driver.switch_to.window(driver.window_handles[1])
                try:
                    driver.switch_to.frame(wait.until(ec.presence_of_element_located((By.ID, 'video-start'))))
                    wait.until(ec.presence_of_element_located((By.ID, 'movie_player'))).click()
                    sleep(time_sleep)
                    driver.switch_to.window(driver.window_handles[0])
                    if not ('С учетом рефбека на ваш счет начислено' in i.text):
                        driver.switch_to.window(driver.window_handles[1])
                        driver.switch_to.frame(wait.until(ec.presence_of_element_located((By.ID, 'video-start'))))
                        wait.until(ec.presence_of_element_located((By.ID, 'movie_player'))).click()
                        sleep(5)
                        driver.switch_to.window(driver.window_handles[1])
                except Exception as e:
                    self.append_log(f'<font color="red">{self.logtime()} {e}</font>')
                    error_count += 1
                    sleep(3)
                else:
                    self.total_earned_money += earned_money
                    self.append_log(f'<font color="green">{self.logtime()} Earned: '
                                    f'{round(earned_money, 5)}, total: {round(self.total_earned_money, 5)}</font>')

                for handle in driver.window_handles[1:]:
                    driver.switch_to.window(handle)
                    driver.close()

                driver.switch_to.window(driver.window_handles[0])
                sleep(1)
        else:
            is_tasks_available = False

        return is_tasks_available

    def log_in(self, driver, login, password):
        self.append_log(f'<font color="">{self.logtime()} Start log in</font>')
        driver.get(f'{self.profitcentr_url}login')

        if False: #exists("profitcentr_cookies"):
            self.append_log(f'<font color="">{self.logtime()} Cookies found</font>')
            for cookie in pload(open("cookies", "rb")):
                driver.add_cookie(cookie)
            driver.get(self.profitcentr_url)
            if 'Статус' in driver.page_source:
                return

        self.append_log(f'<font color="red">{self.logtime()} Error with cookies, manual log in.</font>')
        driver.find_elements(By.CLASS_NAME, "login_vh")[0].send_keys(login)
        sleep(1)
        driver.find_elements(By.CLASS_NAME, "login_vh")[1].send_keys(password)
        while f'{self.profitcentr_url}login' in driver.current_url:
            if driver.find_elements(By.CLASS_NAME, 'out-capcha'):
                self.append_log(f'<font color="red">{self.logtime()} COMPLETE THE CAPTCHA</font>')
            else:
                self.append_log(f'<font color="orange">{self.logtime()} Waiting for log in</font>')
            sleep(1)

        pdump(driver.get_cookies(), open("profitcentr_cookies", "wb"))
        self.append_log(f'<font color="">{self.logtime()} Finished log in</font>')
