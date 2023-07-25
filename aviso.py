from selenium.webdriver.common.by import By

from os.path import exists
import datetime
import pickle
import time

from res.string import strings
from bcolors import bcolors
from browser import Browser


def _is_captcha_available(driver):
    if len(driver.find_elements(By.ID, 'h-captcha')) != 0 or len(driver.find_elements(By.CLASS_NAME, 'captcha')):
        return True
    else:
        return False


class Aviso:
    def __init__(self, settings):
        self.aviso_url = "https://aviso.bz/"
        self.total_earned_money = 0
        self.settings = settings.get_settings()
        self.lan = self.settings['language']

    def view_websites(self, driver):
        print(f"{datetime.datetime.now()} " +
              f"{strings['view_web'][self.lan]}"
              )
        driver.get("https://wmrfast.com/serfingnew.php")
        print(f'{datetime.datetime.now()} sleep {5} seconds')
        time.sleep(5)
        if _is_captcha_available(driver):
            input(f'\n\n\n{bcolors.WARNING}WARNING, COMPLETE THE CAPTCHA AND PRESS ENTER{bcolors.ENDC}\n\n\n')

        website_list = driver.find_elements(By.CLASS_NAME, "no_active_link")
        is_tasks_available = True
        if len(website_list) > 0:
            for i in website_list:
                try:
                    a = i.find_element(By.CLASS_NAME, "serf_hash")
                    price_span, time_span = i.find_elements(By.CLASS_NAME, "clickprice")
                    earned_money = float(price_span.get_attribute('innerHTML'))
                    time_sleep = int(time_span.get_attribute('innerHTML').split()[0]) + 5
                    if 't.me' in a.get_attribute('href'):
                        continue
                    else:
                        a.click()
                except Exception as e:
                    print(f"{bcolors.WARNING}{e}{bcolors.ENDC}")
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
                time.sleep(time_sleep)
                self.total_earned_money += earned_money
                print(
                    f"{bcolors.OKGREEN}{datetime.datetime.now()} " +
                    f"{strings['earned'][self.lan]}: " +
                    f"{round(earned_money, 5)}, {strings['total'][self.lan]}: " +
                    f"{round(self.total_earned_money, 5)}{bcolors.ENDC}"
                )
                for handle in driver.window_handles[1:]:
                    driver.switch_to.window(handle)
                    driver.close()

                driver.switch_to.window(driver.window_handles[0])
                time.sleep(5)
        else:
            is_tasks_available = False

        return {
            'is_tasks_available': is_tasks_available,
        }

    def watch_videos(self, driver):
        print(f"{datetime.datetime.now()} " +
              f"{strings['watch_videos'][self.lan]}"
              )

        driver.get("https://aviso.bz/work-youtube")
        if _is_captcha_available(driver):
            input(f'\n\n\n{bcolors.WARNING}WARNING, COMPLETE THE CAPTCHA AND PRESS ENTER{bcolors.ENDC}\n\n\n')
        print(f'{datetime.datetime.now()} sleep {5} seconds')
        time.sleep(5)
        video_list = driver.find_elements(By.CLASS_NAME, "work-serf")
        is_tasks_available = True
        if len(video_list) > 0:
            for i in video_list:
                try:
                    a = i.find_elements(By.TAG_NAME, "span")[0]
                    price_span = i.find_elements(By.TAG_NAME, "span")[4]
                    time_span = i.find_elements(By.TAG_NAME, "span")[6]
                    earned_money = float(price_span.get_attribute('innerHTML').split('<')[0])
                    time_sleep = int(time_span.get_attribute('innerHTML').split()[0])
                    a.click()
                    time.sleep(0.5)
                    i.find_elements(By.CLASS_NAME, 'go-link-youtube')[0].click()
                except Exception as e:
                    print(f"{bcolors.WARNING}{datetime.datetime.now()} {e}{bcolors.ENDC}")
                    time.sleep(5)
                    continue

                for j in range(5):
                    if len(driver.window_handles) < 2:
                        time.sleep(1)
                        continue
                    else:
                        break

                if len(driver.window_handles) < 2:
                    continue

                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(3)
                try:
                    iframe = driver.find_element(By.ID, 'video-start')
                    driver.switch_to.frame(iframe)
                    time.sleep(3)
                    driver.find_element(By.ID, 'movie_player').click()
                    time.sleep(time_sleep + 10)
                    driver.switch_to.window(driver.window_handles[-1])
                    if not ('youtube.com' in driver.current_url):
                        iframe = driver.find_element(By.ID, 'video-start')
                        driver.switch_to.frame(iframe)
                        time.sleep(3)
                        driver.find_element(By.ID, 'movie_player').click()
                        time.sleep(7)
                        driver.switch_to.window(driver.window_handles[-1])

                    self.total_earned_money += earned_money
                    print(
                        f"{bcolors.OKGREEN}{datetime.datetime.now()} " +
                        f"{strings['earned'][self.lan]}: " +
                        f"{round(earned_money, 5)}, {strings['total'][self.lan]}: " +
                        f"{round(self.total_earned_money, 5)}{bcolors.ENDC}"
                        )
                except Exception as e:
                    print(f"{bcolors.WARNING}{datetime.datetime.now()}{e}{bcolors.ENDC}")
                    time.sleep(5)

                for handle in driver.window_handles[1:]:
                    driver.switch_to.window(handle)
                    driver.close()

                driver.switch_to.window(driver.window_handles[0])
                time.sleep(3)
        else:
            is_tasks_available = False

        return {
            'is_tasks_available': is_tasks_available,
        }

    def log_in(self):
        print(f"{datetime.datetime.now()} {strings['start_log_in'][self.lan]}")
        driver = Browser(self.settings['browser_is_headless']
                         ).open_browser() if exists("cookies") else Browser(False).open_browser()

        driver.get(self.aviso_url)

        if exists("cookies"):
            print(f"{datetime.datetime.now()} {strings['cookies_find'][self.lan]}")
            for cookie in pickle.load(open("cookies", "rb")):
                driver.add_cookie(cookie)
            driver.get(self.aviso_url)
        else:
            print(f"{datetime.datetime.now()} {strings['cookies_not_find'][self.lan]}")
            file = open("authentication_data.txt", "r")
            auth_data = file.read().split(":")
            file.close()

            if len(auth_data) == 2:
                login, password = auth_data
            else:
                login, password = "", ""

            time.sleep(5)

            driver.find_element(By.CLASS_NAME, "button-login").click()
            time.sleep(3)
            driver.find_elements(By.CLASS_NAME, "form-control")[0].send_keys(login)
            time.sleep(1)
            driver.find_elements(By.CLASS_NAME, "form-control")[1].send_keys(password)
            del auth_data, login, password
            input(f"{datetime.datetime.now()} Press ENTER after log in")

            pickle.dump(driver.get_cookies(), open("cookies", "wb"))
        print(f"{datetime.datetime.now()} {strings['finish_log_in'][self.lan]}")

        return driver
