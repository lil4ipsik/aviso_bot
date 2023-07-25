from selenium import webdriver


class Browser:
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
