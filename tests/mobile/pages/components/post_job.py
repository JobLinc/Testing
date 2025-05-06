from appium.webdriver.common.appiumby import AppiumBy
from ..base_page import BasePage


class PostJobPage(BasePage):
    """Page object for the create job screen."""

    PAGE_TITLE = (AppiumBy.ACCESSIBILITY_ID, "Create Job")

    def verify_page_loaded(self, timeout: int = 15) -> None:
        """Ensures the create job screen is loaded by checking the page title."""
        self.wait_for_element(self.PAGE_TITLE, timeout)
