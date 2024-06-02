from os.path import exists
from pickle import dump as pdump, load as pload
from time import sleep

from colorama import just_fix_windows_console
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from business import logtime
from web_bot import WebBot

load_dotenv()
just_fix_windows_console()

AVISO_URL = "https://aviso.bz/"

def _is_captcha_available(driver):
    if len(driver.find_elements(By.ID, 'h-captcha')) != 0 or len(driver.find_elements(By.CLASS_NAME, 'captcha')):
        return True
    else:
        return False


class Aviso(WebBot):
    def __int__(self):
        pass

    def get_balance(self):
        return self.total_earned_money

    def view_websites(self, driver):
        self.append_log(f'<font color="">{logtime()} Surf web</font>')
        self.wait_while_paused()
        driver.get("https://aviso.bz/work-serf")
        self.wait_while_paused()
        if driver.find_elements(By.CLASS_NAME, "form-control"):
            self.log_in()
        error_count = 0
        website_list = driver.find_elements(By.CLASS_NAME, "work-serf")
        is_tasks_available = True
        if len(website_list) > 0:
            for i in website_list:
                self.wait_while_paused()
                if error_count >= 3:
                    return False
                try:
                    a = i.find_element(By.TAG_NAME, "a")
                    price_span = i.find_element(By.XPATH, 'tbody/tr/td[3]/span[2]')
                    time_span = i.find_element(By.XPATH, "tbody/tr/td[3]/div/span[1]")
                    earned_money = float(price_span.get_attribute('innerHTML').split('<')[0])
                    time_sleep = int(time_span.get_attribute('innerHTML').split()[0]) + 5
                    self.wait_while_paused()
                    a.click()
                    sleep(1.5)
                    i.find_element(By.CLASS_NAME, 'start-yes-serf').click()
                except Exception as e:
                    self.append_log(f'<font color="red">{logtime()} {e}</font>')
                    error_count += 1
                    continue

                for j in range(5):
                    self.wait_while_paused()
                    if len(driver.window_handles) < 2:
                        sleep(1)
                        continue
                    else:
                        break

                if len(driver.window_handles) < 2:
                    continue

                try:
                    self.wait_while_paused()
                    driver.switch_to.window(driver.window_handles[1])
                    sleep(time_sleep)
                    driver.switch_to.frame('frminfo')
                    self.wait_while_paused()
                    driver.find_element(By.TAG_NAME, 'a').click()
                except Exception as e:
                    self.append_log(f'<font color="red">{logtime()} {e}</font>')
                    error_count += 1
                    sleep(3)
                else:
                    sleep(0.5)
                    self.total_earned_money += earned_money
                    self.total_earned_money += earned_money
                    self.append_log(f'<font color="green">{logtime()} Earned: '
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
        self.append_log(f'<font color="">{logtime()} Watch YouTube</font>')
        self.wait_while_paused()
        driver.get("https://aviso.bz/work-youtube")
        while _is_captcha_available(driver):
            self.append_log(f'<font color="red">{logtime()} WARNING, COMPLETE THE CAPTCHA</font>')
            sleep(1)
        wait = WebDriverWait(driver, 7)
        error_count = 0
        video_list = []
        if driver.find_elements(By.CLASS_NAME, "form-control"):
            self.log_in()
        for task in driver.find_elements(By.CLASS_NAME, "work-serf"):
            if 'Просмотр видеоролика' in task.text:
                video_list.append(task)
        is_tasks_available = True if video_list else False
        if len(video_list) > 0:
            for i in video_list:
                self.wait_while_paused()
                if error_count >= 3:
                    return False
                try:
                    a = i.find_element(By.TAG_NAME, "span")
                    price_span = i.find_element(By.XPATH, "tbody/tr/td[3]/span[2]")
                    time_span = i.find_element(By.XPATH, "tbody/tr/td[3]/div/span[1]")
                    earned_money = float(price_span.get_attribute('innerHTML').split('<')[0])
                    time_sleep = int(time_span.get_attribute('innerHTML').split()[0]) + 3
                    self.wait_while_paused()
                    a.click()
                    sleep(1.5)
                except Exception as e:
                    self.append_log(f'<font color="red">{logtime()} {e}</font>')
                    error_count += 1
                    continue

                for j in range(5):
                    self.wait_while_paused()
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
                    self.wait_while_paused()
                    wait.until(ec.presence_of_element_located((By.ID, 'movie_player'))).click()
                    sleep(time_sleep)
                    driver.switch_to.window(driver.window_handles[0])
                    if not ('С учетом рефбека на ваш счет начислено' in i.text):
                        driver.switch_to.window(driver.window_handles[1])
                        driver.switch_to.frame(wait.until(ec.presence_of_element_located((By.ID, 'video-start'))))
                        self.wait_while_paused()
                        wait.until(ec.presence_of_element_located((By.ID, 'movie_player'))).click()
                        sleep(5)
                        driver.switch_to.window(driver.window_handles[1])
                except Exception as e:
                    self.append_log(f'<font color="red">{logtime()} {e}</font>')
                    error_count += 1
                    sleep(3)
                else:
                    self.total_earned_money += earned_money
                    self.append_log(f'<font color="green">{logtime()} Earned: '
                                        f'{round(earned_money, 5)}, total: {round(self.total_earned_money, 5)}</font>')

                for handle in driver.window_handles[1:]:
                    driver.switch_to.window(handle)
                    driver.close()

                driver.switch_to.window(driver.window_handles[0])
                sleep(1)
        else:
            is_tasks_available = False

        return is_tasks_available

    def log_in(self):
        self.append_log(f'<font color="">{logtime()} Start log in</font>')
        self.wait_while_paused()
        self.driver.get(AVISO_URL)
        if exists(f"aviso_{self.login}_cookies"):
            self.append_log(f'<font color="">{logtime()} Cookies found</font>')
            for cookie in pload(open(f"aviso_{self.login}_cookies", "rb")):
                self.driver.add_cookie(cookie)
            self.wait_while_paused()
            self.driver.get(AVISO_URL)
            if 'Статус' in self.driver.page_source:
                return

        self.append_log(f'<font color="red">{logtime()} Error with cookies, manual log in.</font>')
        self.wait_while_paused()
        self.driver.find_element(By.CLASS_NAME, "button-login").click()
        sleep(3)
        self.driver.find_elements(By.CLASS_NAME, "form-control")[0].send_keys(self.login)
        sleep(1)
        self.driver.find_elements(By.CLASS_NAME, "form-control")[1].send_keys(self.password)
        sleep(1)
        self.wait_while_paused()
        self.driver.find_element(By.ID, 'button-login').click()
        self.wait_while_paused()
        while "https://aviso.bz/login" in self.driver.current_url:
            if self.driver.find_elements(By.ID, 'anchor'):
                self.append_log(f'<font color="red">{logtime()} COMPLETE THE CAPTCHA</font>')
            else:
                self.append_log(f'<font color="orange">{logtime()} Waiting for log in</font>')
            sleep(1)

        self.wait_while_paused()
        pdump(self.driver.get_cookies(), open(f"aviso_{self.login}_cookies", "wb"))
        self.append_log(f'<font color="">{logtime()} Finished log in</font>')
