from abc import ABC, abstractmethod
from typing import Self
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement as AppiumWebElement
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging


class BasePage(ABC):
    """Enhanced base page with state management and fluent interface"""

    def __init__(self, driver: WebDriver, verify_page: bool = True) -> None:
        self.driver: WebDriver = driver
        self.logger: logging.Logger = logging.getLogger(__name__)

        if verify_page:
            try:
                self.verify_page_loaded()
            except TimeoutException:
                raise PageNavigationError("Page didn't successfully load")

    @abstractmethod
    def verify_page_loaded(self, timeout: int = 15) -> None:
        """Verify the page is loaded using page-specific elements"""
        pass

    def is_current_page(self, timeout: int = 5) -> bool:
        """Check if this page is currently active"""
        try:
            self.verify_page_loaded(timeout)
            return True
        except TimeoutException:
            return False

    def navigate_to(self, page_class: type[Self], *args, **kwargs) -> Self:
        """Navigate to another page and return its instance"""
        new_page = page_class(self.driver, *args, **kwargs)
        if not new_page.is_current_page():
            raise PageNavigationError(
                f"Failed to navigate to {page_class.__name__}"
            )
        return new_page

    def wait_for_element(
        self, locator: tuple[str, str], timeout: int = 15
    ) -> AppiumWebElement:
        """Smart wait for element presence"""
        self.logger.info(f"Waiting for element: {locator}")
        return WebDriverWait(self.driver, timeout).until(  # type: ignore
            EC.presence_of_element_located(locator)
        )

    def click(self, locator: tuple[str, str]) -> Self:
        """Fluent interface click with built-in wait"""
        self.wait_for_element(locator).click()
        return self

    def enter_text(self, locator: tuple[str, str], text: str) -> Self:
        """Fluent text entry with validation"""
        element = self.wait_for_element(locator)
        element.click()
        element.clear()
        element.send_keys(text)
        self.driver.hide_keyboard()
        return self

    def choose_dropdown(self, dropdown_location: tuple[str, str], choice: str):
        """
        Selects an option from a dropdown menu with scrolling capability.

        Args:
            dropdown_location: Tuple containing the locator strategy and value to find the dropdown element
            choice: The text of the option to select from the dropdown
        """
        dropdown_element = self.driver.find_element(*dropdown_location)
        dropdown_element.click()

        try:
            option_element = self.driver.find_element(
                AppiumBy.XPATH,
                f'//android.widget.Button[@content-desc="{choice}"]',
            )
            option_element.click()
            return
        except:
            pass

        previous_page_source = ""
        max_scrolls = 10

        for _ in range(max_scrolls):
            current_page_source = self.driver.page_source

            try:
                option_element = self.driver.find_element(
                    AppiumBy.XPATH,
                    f'//android.widget.Button[@content-desc="{choice}"]',
                )
                option_element.click()
                return
            except:
                if current_page_source == previous_page_source:
                    break

                screen_size = self.driver.get_window_size()
                start_x = screen_size["width"] // 2
                start_y = screen_size["height"] * 2 // 3
                end_y = screen_size["height"] // 3

                self.driver.swipe(start_x, start_y, start_x, end_y, 500)

                previous_page_source = current_page_source

        try:
            option_element = self.driver.find_element(
                AppiumBy.XPATH,
                f'//android.widget.Button[@content-desc="{choice}"]',
            )
            option_element.click()
        except:
            raise Exception(f"Could not find option '{choice}' in the dropdown")

    def take_screenshot(self, name: str) -> Self:
        """Take screenshot and continue chain"""
        self.driver.save_screenshot(f"{name}.png")
        return self

    def wait_for_toast_to_appear(
        self, toast_text: str, timeout: int = 7
    ) -> AppiumWebElement:
        """
        Wait for toast containing that text.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(  # type: ignore
                EC.presence_of_element_located(
                    (AppiumBy.ACCESSIBILITY_ID, toast_text)
                )
            )
        except TimeoutException:
            raise TimeoutException(
                f"Toast with text '{toast_text}' not found within {timeout} seconds"
            )


class PageNavigationError(Exception):
    """Custom exception for page navigation failures"""

    pass
