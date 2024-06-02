import random
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

from business import logtime
from web_bot import WebBot

load_dotenv()
just_fix_windows_console()

PROFITCENTR_URL = "https://profitcentr.com/"


def _is_captcha_available(driver):
    if len(driver.find_elements(By.ID, 'out-capcha')) != 0 or len(
            driver.find_elements(By.CLASS_NAME, 'out-capcha')) != 0:
        return True
    else:
        return False


class Profitcentr(WebBot):
    def __int__(self):
        pass

    def get_balance(self):
        return self.total_earned_money

    def view_websites(self, driver):
        self.append_log(f'<font color="">{logtime()} Surf web</font>')
        min_video_count = 50
        max_video_count = 100
        wait = WebDriverWait(driver, 7)
        self.wait_while_paused()
        if wait.until(ec.presence_of_element_located((By.ID, 'mnu_tblock1'))).value_of_css_property("display") == "none":
            self.wait_while_paused()
            driver.find_element(By.ID, 'mnu_title1').click()
            time.sleep(3)
        self.wait_while_paused()
        driver.find_element(By.ID, 'mnu_tblock1').find_elements(By.TAG_NAME, 'a')[1].click()
        time.sleep(3)
        self.wait_while_paused()
        while _is_captcha_available(driver):
            self.append_log(f'<font color="red">{logtime()} COMPLETE CAPTCHA</font>')
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
                                          driver.page_source):
            for i in website_list[:random.randint(min_video_count, max_video_count)]:
                self.wait_while_paused()
                while _is_captcha_available(driver):
                    self.append_log(f'<font color="red">{logtime()} COMPLETE CAPTCHA</font>')
                    time.sleep(1)
                if error_count >= 3:
                    return False
                try:
                    a = i.find_element(By.TAG_NAME, "a")
                    price_span = i.find_element(By.XPATH, 'tbody/tr/td[3]/span[2]')
                    time_span = i.find_element(By.XPATH, "tbody/tr/td[2]/div[1]/a")
                    print(price_span.get_attribute('innerHTML').split(' ')[0],
                          time_span.get_attribute('onclick').replace("'", '').split(',')[2])
                    earned_money = float(price_span.get_attribute('innerHTML').split(' ')[0])
                    time_sleep = int(time_span.get_attribute('onclick').replace("'", '').split(',')[2]) + 5
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

                try:
                    driver.switch_to.window(driver.window_handles[1])
                    sleep(time_sleep)
                except Exception as e:
                    self.append_log(f'<font color="red">{logtime()} {e}</font>')
                    error_count += 1
                    sleep(3)
                else:
                    sleep(0.5)
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
        self.append_log(f'<font color="">{logtime()} Watch youtube</font>')
        min_video_count = 75
        max_video_count = 100
        current_video_count = random.randint(min_video_count, max_video_count)
        wait = WebDriverWait(driver, 7)
        self.wait_while_paused()
        if wait.until(ec.presence_of_element_located((By.ID, 'mnu_tblock1'))).value_of_css_property("display") == "none":
            driver.find_element(By.ID, 'mnu_title1').click()
            time.sleep(3)
        driver.find_element(By.ID, 'mnu_tblock1').find_elements(By.TAG_NAME, 'a')[5].click()
        time.sleep(3)
        self.wait_while_paused()
        while _is_captcha_available(driver):
            self.append_log(f'<font color="red">{logtime()} COMPLETE CAPTCHA</font>')
            time.sleep(1)
        time.sleep(5)
        error_count = 0
        video_list = driver.find_elements(By.CLASS_NAME, "work-serf")
        is_tasks_available = True if video_list else False
        for _ in range(current_video_count):
            if len(video_list) == 0:
                for i in range(15):
                    try:
                        self.append_log(f'<font color="yellow">{logtime()} {i + 1} try get more videos of 15</font>')
                        self.wait_while_paused()
                        wait.until(ec.presence_of_element_located((By.ID, 'load-pages'))).click()
                        time.sleep(1)
                        # driver.find_element(By.ID, 'load-pages').click()
                        for task in driver.find_elements(By.CLASS_NAME, "work-serf"):
                            if not ('Готово, Вам на счет зачислено' in task.text):
                                video_list.append(task)
                        if len(video_list) != 0:
                            break
                    except Exception as e:
                        self.append_log(f'<font color="red">{logtime()} {e}</font>\nRefresh is normal')
                        driver.refresh()
                        
            if len(video_list) == 0:
                is_tasks_available = False
                break
            self.wait_while_paused()
            while _is_captcha_available(driver):
                self.append_log(f'<font color="red">{logtime()} COMPLETE CAPTCHA</font>')
                time.sleep(1)
            if error_count >= 15:
                is_tasks_available = False
                break
            try:
                self.wait_while_paused()
                video_list[0].find_element(By.TAG_NAME, "span").click()
                sleep(3)
                self.wait_while_paused()
                video_list[0].find_element(By.TAG_NAME, "span").click()
                video_list.pop(0)
            except Exception as e:
                self.append_log(f'<font color="red">{logtime()} {e}</font>')
                error_count += 1
                video_list.pop(0)
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
                time_sleep = int(wait.until(ec.presence_of_element_located((By.ID, 'tmr'))).text) + 5
                driver.switch_to.frame(wait.until(ec.presence_of_element_located((By.ID, 'video-start'))))
                self.wait_while_paused()
                wait.until(ec.presence_of_element_located((By.ID, 'movie_player'))).click()
                sleep(time_sleep)
                driver.switch_to.window(driver.window_handles[1])
                self.wait_while_paused()
                driver.find_element(By.CLASS_NAME, 'butt-nw').click()
                time.sleep(3)
                earned_money = float(wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr[1]'
                                                                                          '/td/table/tbody/tr[2]/td/'
                                                                                          'span/b'))).text)
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
            sleep(random.randint(1, 7))

        return is_tasks_available

    def log_in(self):
        self.append_log(f'<font color="">{logtime()} Start log in</font>')
        self.wait_while_paused()
        self.driver.get(f'{PROFITCENTR_URL}login')

        if exists(f"profitcentr_{self.login}_cookies"):
            self.append_log(f'<font color="">{logtime()} Cookies found</font>')
            for cookie in pload(open(f"profitcentr_{self.login}_cookies", "rb")):
                self.driver.add_cookie(cookie)
            self.wait_while_paused()
            self.driver.get(PROFITCENTR_URL)
            if 'Основной счет' in self.driver.page_source:
                return

        self.append_log(f'<font color="red">{logtime()} Error with cookies, manual log in.</font>')
        self.wait_while_paused()
        self.driver.get(f'{PROFITCENTR_URL}login')
        self.wait_while_paused()
        self.driver.find_elements(By.CLASS_NAME, "login_vh")[0].send_keys(self.login)
        time.sleep(1)
        self.driver.find_elements(By.CLASS_NAME, "login_vh")[1].send_keys(self.password)
        self.wait_while_paused()
        while f'{PROFITCENTR_URL}login' in self.driver.current_url:
            if self.driver.find_elements(By.CLASS_NAME, 'out-capcha'):
                self.append_log(f'<font color="red">{logtime()} COMPLETE THE CAPTCHA</font>')
            else:
                self.append_log(f'<font color="orange">{logtime()} Waiting for log in</font>')
            time.sleep(1)

        time.sleep(10)
        pdump(self.driver.get_cookies(), open(f"profitcentr_{self.login}_cookies", "wb"))
        self.append_log(f'<font color="">{logtime()} Finished log in</font>')
