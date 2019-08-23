from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class PageProperty:

    def __init__(self, driver: WebDriver, element: WebElement):
        self.driver = driver
        self._element = element

    @property
    def element(self) -> WebElement:
        return self._element

    @property
    def is_enabled(self) -> bool:
        return self.element.is_enabled()

    @property
    def is_displayed(self) -> bool:
        return self.element.is_displayed()

    @property
    def text(self) -> str:
        return self.element.text

    def click(self) -> None:
        self.element.click()

    def get_attribute(self, attribute: str) -> Optional[str]:
        return self.element.get_attribute(attribute)
