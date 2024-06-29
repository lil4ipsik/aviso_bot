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
from twocaptcha import TwoCaptcha

from userdata import *

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
        successful_video_watching_count = 0
        wait = WebDriverWait(driver, 5)
        self.wait_while_paused()
        if wait.until(ec.presence_of_element_located((By.ID, 'mnu_tblock1'))).value_of_css_property("display") == "none":
            self.wait_while_paused()
            wait.until(ec.presence_of_element_located((By.ID, 'mnu_title1'))).click()
        self.wait_while_paused()
        wait.until(ec.presence_of_element_located((By.ID, 'mnu_tblock1'))).find_elements(By.TAG_NAME, 'a')[1].click()
        time.sleep(3)
        self.wait_while_paused()
        while _is_captcha_available(driver):
            self.append_log(f'<font color="red">{logtime()} COMPLETE CAPTCHA</font>')
            time.sleep(1)
        error_count = 0
        website_list = driver.find_elements(By.CLASS_NAME, "work-serf")
        print(website_list)
        if len(website_list) > 0 and not ('Нет переходов доступных для просмотра, зайдите немного позже' in
                                          driver.page_source):
            for i in website_list[:random.randint(min_video_count, max_video_count)]:
                self.wait_while_paused()
                while _is_captcha_available(driver):
                    self.append_log(f'<font color="red">{logtime()} COMPLETE CAPTCHA</font>')
                    time.sleep(1)
                if error_count >= 15:
                    break
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
                        sleep(0.25)
                        continue
                    else:
                        break

                if len(driver.window_handles) < 2:
                    continue

                try:
                    driver.switch_to.window(driver.window_handles[1])
                    sleep(time_sleep + 3)
                except Exception as e:
                    self.append_log(f'<font color="red">{logtime()} {e}</font>')
                    error_count += 1
                    sleep(0.25)
                else:
                    successful_video_watching_count += 1
                    self.total_earned_money += earned_money
                    self.append_log(f'<font color="green">{logtime()} Earned: '
                                    f'{round(earned_money, 5)}, total: {round(self.total_earned_money, 5)}</font>')
                for handle in driver.window_handles[1:]:
                    driver.switch_to.window(handle)
                    driver.close()

                driver.switch_to.window(driver.window_handles[0])
                sleep(1)

        return True if successful_video_watching_count > 0 else False

    def watch_videos(self, driver):
        self.append_log(f'<font color="">{logtime()} Watch youtube</font>')
        min_video_count = 75
        max_video_count = 150
        successful_video_watching_count = 0
        current_video_count = random.randint(min_video_count, max_video_count)
        wait = WebDriverWait(driver, 5)
        self.wait_while_paused()
        if wait.until(ec.presence_of_element_located((By.ID, 'mnu_tblock1'))).value_of_css_property("display") == "none":
            wait.until(ec.presence_of_element_located((By.ID, 'mnu_title1'))).click()
            time.sleep(0.25)
        wait.until(ec.presence_of_element_located((By.ID, 'mnu_tblock1'))).find_elements(By.TAG_NAME, 'a')[5].click()
        time.sleep(3)
        self.wait_while_paused()
        self._solve_captcha('btn')
        error_count = 0
        video_list = driver.find_elements(By.CLASS_NAME, "work-serf")
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
                            if 'Просмотр видеоролика' in task.text:
                                video_list.append(task)
                        if len(video_list) != 0:
                            break
                    except Exception as e:
                        self.append_log(f'<font color="red">{logtime()} {e}</font>\nRefresh is normal')
                        driver.refresh()
                        time.sleep(3)
                        
            if len(video_list) == 0:
                break
            self.wait_while_paused()
            self._solve_captcha('btn')
            if error_count >= 15:
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
                wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'butt-nw'))).click()
                # driver.find_element(By.CLASS_NAME, 'butt-nw').click()
                time.sleep(3)
                earned_money = float(wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr[1]'
                                                                                          '/td/table/tbody/tr[2]/td/'
                                                                                          'span/b'))).text)
            except Exception as e:
                self.append_log(f'<font color="red">{logtime()} {e}</font>')
                error_count += 1
                sleep(3)
            else:
                successful_video_watching_count += 1
                self.total_earned_money += earned_money
                self.append_log(f'<font color="green">{logtime()} Earned: '
                                f'{round(earned_money, 5)}, total: {round(self.total_earned_money, 5)}</font>')

            for handle in driver.window_handles[1:]:
                driver.switch_to.window(handle)
                driver.close()

            driver.switch_to.window(driver.window_handles[0])
            sleep(random.randint(1, 3))

        return True if successful_video_watching_count > 0 else False
    
    def dump_cookies(self, driver):
        self.file_path = path_to_cookies(self)
        pdump(driver.get_cookies(),
            open(self.file_path, "wb"))

    def log_in(self):
        self.append_log(f'<font color="">{logtime()} Start log in</font>')
        self.wait_while_paused()
        self.driver.get(f'{PROFITCENTR_URL}login')

        self.file_path = path_to_cookies(self)
        if exists(self.file_path):
            self.append_log(f'<font color="">{logtime()} Cookies found</font>')
            for cookie in pload(open(self.file_path, "rb")):
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
        self._solve_captcha('btn_big_green')
        while f'{PROFITCENTR_URL}login' in self.driver.current_url:
            self.append_log(f'<font color="orange">{logtime()} Waiting for log in</font>')
            time.sleep(1)
        time.sleep(10)
        self.dump_cookies(self.driver)
        self.append_log(f'<font color="">{logtime()} Finished log in</font>')

    def _solve_captcha(self, button_class):
        while True:
            config = {
                'server': '2captcha.com',
                'apiKey': get_api_key(),
                'softId': 123321111,
                'defaultTimeout': 120,
                'recaptchaTimeout': 600,
            }
            solver = TwoCaptcha(**config)
            try:
                self.driver.find_element(By.CLASS_NAME, 'out-reload').click()
                time.sleep(1)
                self.driver.find_element(By.CLASS_NAME, 'out-capcha').screenshot('screen.png')
            except Exception as e:
                print(e)
                return
            print(self.driver.find_element(By.CLASS_NAME, 'out-capcha-title').text)
            try:
                result = solver.grid(file='screen.png', hintText=self.driver.find_element(
                    By.CLASS_NAME, 'out-capcha-title').text, cols=6, rows=1, lang='ru')
                print(result)
            except Exception as e:
                print(e)
                self.driver.find_element(By.CLASS_NAME, 'out-reload').click()
                time.sleep(1)
                continue
            for index in result['code'].split(':')[1].split('/'):
                print(index)
                time.sleep(random.randint(1, 15) / 10)
                self.driver.find_elements(By.CLASS_NAME, 'out-capcha-lab')[int(index) - 1].click()
            print('sleep after for')
            time.sleep(1)
            self.driver.find_element(By.CLASS_NAME, button_class).click()
            print('good click to button')
            time.sleep(10)
            if _is_captcha_available(self.driver):
                solver.report(result['captchaId'], False)
            else:
                break



