from appium.webdriver.common.appiumby import AppiumBy

from ...base_page import BasePage
from .login_page import LoginPage
from .register_page import RegisterPage


class LandingPage(BasePage):
    """Page object for the landing screen before login."""

    SIGN_IN_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Sign in with email ")',
    )

    AGREE_AND_JOIN = (AppiumBy.ACCESSIBILITY_ID, "Agree & Join")

    def verify_page_loaded(self, timeout: int = 15) -> None:
        """Ensures the landing screen is loaded by checking the sign-in button."""
        self.wait_for_element(self.SIGN_IN_BUTTON, timeout)

    def go_to_login(self) -> LoginPage:
        """Clicks 'Sign in with email' and navigates to LoginPage."""
        self.click(self.SIGN_IN_BUTTON)
        return LoginPage(self.driver)

    def go_to_register(self) -> RegisterPage:
        """Clicks 'Agree & Join' and navigates to RegisterPage."""
        self.click(self.AGREE_AND_JOIN)
        return RegisterPage(self.driver)
