from appium.webdriver.common.appiumby import AppiumBy
from ...base_page import BasePage
from .change_password_page import ChangePasswordPage


class SettingsPage(BasePage):
    """Page object for the settings screen."""

    CHANGE_PASSWORD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Change Password")',
    )
    LOGOUT_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Logout")',
    )

    def verify_page_loaded(self, timeout: int = 5) -> None:
        """Ensure the settings page is loaded."""
        self.wait_for_element(self.CHANGE_PASSWORD, timeout)

    def navigate_to_change_password(self) -> ChangePasswordPage:
        self.click(self.CHANGE_PASSWORD)
        return ChangePasswordPage(self.driver)

    def logout(self):
        """Perform logout action and return the Login page."""
        self.click(self.LOGOUT_BUTTON)

        # Import inside the method to avoid circular import
        from ..auth.login_page import LoginPage

        return LoginPage(self.driver)
