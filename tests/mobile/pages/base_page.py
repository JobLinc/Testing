from typing import Tuple
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement


class BasePage:
    """Base class for mobile pages with common actions."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        """Find an element by locator (ID, XPath, etc.)."""
        return self.driver.find_element(*locator)

    def find_by_accessibility_id(self, accessibility_id: str) -> WebElement:
        """Find an element using Accessibility ID."""
        return self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, accessibility_id
        )

    def find_by_xpath(self, xpath: str) -> WebElement:
        """Find an element using XPath."""
        return self.driver.find_element(AppiumBy.XPATH, xpath)

    def find_by_classname(self, classname: str) -> WebElement:
        """Find an element using class name."""
        return self.driver.find_element(AppiumBy.CLASS_NAME, classname)

    def click(self, locator: Tuple[str, str]) -> None:
        """Click an element."""
        self.find_element(locator).click()

    def click_by_accessibility_id(self, accessibility_id: str) -> None:
        """Click an element using Accessibility ID."""
        self.find_by_accessibility_id(accessibility_id).click()

    def click_by_xpath(self, xpath: str) -> None:
        """Click an element using XPath."""
        self.find_by_xpath(xpath).click()

    def enter_text(self, locator: Tuple[str, str], text: str) -> None:
        """Enter text into an input field."""
        element = self.find_element(locator)
        element.click()
        element.clear()
        element.send_keys(text)
        self.driver.hide_keyboard()

    def enter_text_by_accessibility_id(
        self, accessibility_id: str, text: str
    ) -> None:
        """Enter text using Accessibility ID."""
        element = self.find_by_accessibility_id(accessibility_id)
        element.click()
        element.clear()
        element.send_keys(text)
        self.driver.hide_keyboard()

    def enter_text_by_xpath(self, xpath: str, text: str) -> None:
        """Enter text using XPath."""
        element = self.find_by_xpath(xpath)
        element.click()
        element.clear()
        element.send_keys(text)
        self.driver.hide_keyboard()
