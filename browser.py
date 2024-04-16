from selenium import webdriver


class Firefox:
    def __init__(self, is_headless=False):
        self.driver = None
        self.options = webdriver.FirefoxOptions()
        self.options.headless = is_headless
        self.options.set_preference("media.volume_scale", "0.0")
        self.options.set_preference('intl.accept_languages', 'ru')
        self.options.set_preference("dom.webdriver.enabled", False)
        self.options.set_preference('useAutomationExtension', False)

    def open_browser(self):
        driver = webdriver.Firefox(options=self.options)
        self.driver = driver
        return driver


class Chrome:
    def __init__(self, is_headless=False):
        self.driver = None
        self.options = webdriver.ChromeOptions()
        self.options.headless = is_headless
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--disable-infobars")
        self.options.add_argument("--disable-notifications")
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument("--mute-audio")

    def open_browser(self):
        driver = webdriver.Chrome(options=self.options)
        self.driver = driver
        return driver
