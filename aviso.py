import datetime
import pickle
import time
from os.path import exists

from colorama import just_fix_windows_console
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()
just_fix_windows_console()


def _is_captcha_available(driver):
    if len(driver.find_elements(By.ID, 'h-captcha')) != 0 or len(driver.find_elements(By.CLASS_NAME, 'captcha')):
        return True
    else:
        return False


class Aviso:
    def __init__(self, exit_event, ui,log_box):
        self.aviso_url = "https://aviso.bz/"
        self.total_earned_money = 0
        self.exit_event = exit_event
        self.ui = ui
        self.log_box = log_box

    def get_balance(self):
        return self.total_earned_money

    def view_websites(self, driver):
        while self.exit_event.is_set():
            time.sleep(1)
        self.log_box.append(f'<font color="">{datetime.datetime.now()} serf web</font>')
        driver.get("https://aviso.bz/work-serf")
        while self.exit_event.is_set():
            time.sleep(1)
        self.log_box.append(f'<font color="">{datetime.datetime.now()} watch youtube</font>')

        if driver.find_elements(By.CLASS_NAME, "form-control"):
            self.log_in(driver, self.ui.login_edit.text(), self.ui.password_edit.text())
        error_count = 0
        website_list = driver.find_elements(By.CLASS_NAME, "work-serf")
        is_tasks_available = True
        if len(website_list) > 0:
            for i in website_list:
                while self.exit_event.is_set():
                    time.sleep(1)
                if error_count >= 3:
                    return False
                try:
                    a = i.find_element(By.TAG_NAME, "a")
                    price_span = i.find_element(By.XPATH, 'tbody/tr/td[3]/span[2]')
                    time_span = i.find_element(By.XPATH, "tbody/tr/td[3]/div/span[1]")
                    earned_money = float(price_span.get_attribute('innerHTML').split('<')[0])
                    time_sleep = int(time_span.get_attribute('innerHTML').split()[0]) + 5
                    a.click()
                    time.sleep(1.5)
                    i.find_element(By.CLASS_NAME, 'start-yes-serf').click()
                except Exception as e:
                    self.log_box.append(f'<font color="red">{datetime.datetime.now()} {e}</font>')
                    error_count += 1
                    continue

                for j in range(5):
                    if len(driver.window_handles) < 2:
                        time.sleep(1)
                        continue
                    else:
                        break

                if len(driver.window_handles) < 2:
                    continue

                try:
                    driver.switch_to.window(driver.window_handles[1])
                    time.sleep(time_sleep)
                    driver.switch_to.frame('frminfo')
                    driver.find_element(By.TAG_NAME, 'a').click()
                except Exception as e:
                    self.log_box.append(f'<font color="red">{datetime.datetime.now()} {e}</font>')
                    error_count += 1
                    time.sleep(3)
                else:
                    time.sleep(0.5)
                    self.total_earned_money += earned_money
                    self.total_earned_money += earned_money
                    self.log_box.append(f'<font color="green">{datetime.datetime.now()} earned: '
                                        f'{round(earned_money, 5)}, total: {round(self.total_earned_money, 5)}</font>')
                for handle in driver.window_handles[1:]:
                    driver.switch_to.window(handle)
                    driver.close()

                driver.switch_to.window(driver.window_handles[0])
                time.sleep(1)
        else:
            is_tasks_available = False

        return is_tasks_available

    def watch_videos(self, driver):
        while self.exit_event.is_set():
            time.sleep(1)
        self.log_box.append(f'<font color="">{datetime.datetime.now()} watch youtube</font>')

        driver.get("https://aviso.bz/work-youtube")
        while _is_captcha_available(driver):
            self.log_box.append(f'<font color="red">{datetime.datetime.now()} WARNING, COMPLETE THE CAPTCHA</font>')
            time.sleep(1)
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
                    time.sleep(1)
                if error_count >= 3:
                    return False
                try:
                    a = i.find_element(By.TAG_NAME, "span")
                    price_span = i.find_element(By.XPATH, "tbody/tr/td[3]/span[2]")
                    time_span = i.find_element(By.XPATH, "tbody/tr/td[3]/div/span[1]")
                    earned_money = float(price_span.get_attribute('innerHTML').split('<')[0])
                    time_sleep = int(time_span.get_attribute('innerHTML').split()[0]) + 3
                    a.click()
                    time.sleep(1.5)
                except Exception as e:
                    self.log_box.append(f'<font color="red">{datetime.datetime.now()} {e}</font>')
                    error_count += 1
                    continue

                for j in range(5):
                    if len(driver.window_handles) < 2:
                        time.sleep(1)
                        continue
                    else:
                        break

                if len(driver.window_handles) < 2:
                    continue

                driver.switch_to.window(driver.window_handles[1])
                try:
                    driver.switch_to.frame(wait.until(ec.presence_of_element_located((By.ID, 'video-start'))))
                    wait.until(ec.presence_of_element_located((By.ID, 'movie_player'))).click()
                    time.sleep(time_sleep)
                    driver.switch_to.window(driver.window_handles[0])
                    if not ('С учетом рефбека на ваш счет начислено' in i.text):
                        driver.switch_to.window(driver.window_handles[1])
                        driver.switch_to.frame(wait.until(ec.presence_of_element_located((By.ID, 'video-start'))))
                        wait.until(ec.presence_of_element_located((By.ID, 'movie_player'))).click()
                        time.sleep(5)
                        driver.switch_to.window(driver.window_handles[1])
                except Exception as e:
                    self.log_box.append(f'<font color="red">{datetime.datetime.now()} {e}</font>')
                    error_count += 1
                    time.sleep(3)
                else:
                    self.total_earned_money += earned_money
                    self.log_box.append(f'<font color="green">{datetime.datetime.now()} earned: '
                                        f'{round(earned_money, 5)}, total: {round(self.total_earned_money, 5)}</font>')

                for handle in driver.window_handles[1:]:
                    driver.switch_to.window(handle)
                    driver.close()

                driver.switch_to.window(driver.window_handles[0])
                time.sleep(1)
        else:
            is_tasks_available = False

        return is_tasks_available

    def log_in(self, driver,  login, password):
        self.log_box.append(f'<font color="">{datetime.datetime.now()} start log in</font>')
        driver.get(self.aviso_url)

        if exists("cookies"):
            self.log_box.append(f'<font color="">{datetime.datetime.now()} cookies find</font>')
            for cookie in pickle.load(open("cookies", "rb")):
                driver.add_cookie(cookie)
            driver.get(self.aviso_url)
            if 'Статус' in driver.page_source:
                return

        self.log_box.append(f'<font color="red">{datetime.datetime.now()} error with cookies. Manual og in</font>')
        driver.find_element(By.CLASS_NAME, "button-login").click()
        time.sleep(3)
        driver.find_elements(By.CLASS_NAME, "form-control")[0].send_keys(login)
        time.sleep(1)
        driver.find_elements(By.CLASS_NAME, "form-control")[1].send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID, 'button-login').click()
        while "https://aviso.bz/login" in driver.current_url:
            if driver.find_elements(By.ID, 'anchor'):
                self.log_box.append(f'<font color="red">{datetime.datetime.now()} COMPLETE THE CAPTCHA</font>')
            else:
                self.log_box.append(f'<font color="orange">{datetime.datetime.now()} wait for log in</font>')
            time.sleep(1)

        pickle.dump(driver.get_cookies(), open("cookies", "wb"))
        self.log_box.append(f'<font color="">{datetime.datetime.now()} finish log in</font>')
