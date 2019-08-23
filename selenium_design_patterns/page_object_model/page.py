from selenium.webdriver.remote.webdriver import WebDriver


class Page:

    def __init__(self, driver: WebDriver):
        self.driver = driver
