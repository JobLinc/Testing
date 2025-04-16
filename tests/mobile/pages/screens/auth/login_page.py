from typing import Self

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from ...base_page import BasePage, PageNavigationError
from ..home_page import HomePage


class LoginPage(BasePage):
    """Page object for the login screen."""

    EMAIL_INPUT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(0)',
    )

    PASSWORD_INPUT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)',
    )

    CONTINUE_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Continue")',
    )

    EMPTY_EMAIL_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Please enter your email")',
    )

    EMPTY_PASSWORD_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Please enter your password")',
    )

    FORGOT_PASSWORD_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Forgot Password?")',
    )

    SUCCESS_TOAST_TEXT = "Login successful"
    FAILURE_TOAST_TEXT = "Incorrect email or password"

    def verify_page_loaded(self, timeout: int = 15) -> None:
        """Ensures the login screen is loaded by waiting for the sign-in button."""
        try:
            self.wait_for_element(self.EMAIL_INPUT, timeout)
            self.wait_for_element(self.PASSWORD_INPUT, timeout)
        except TimeoutException:
            raise PageNavigationError("Login page elements not found")

    def enter_email(self, email: str) -> Self:
        self.enter_text(self.EMAIL_INPUT, email)
        return self

    def enter_password(self, password: str) -> Self:
        self.enter_text(self.PASSWORD_INPUT, password)
        return self

    def navigate_to_forgot_password_page(self):
        from ..auth.forgot_password_page import ForgotPasswordPage

        self.click(self.FORGOT_PASSWORD_BUTTON)
        return ForgotPasswordPage(self.driver)

    def login(self, email: str, password: str) -> HomePage:
        """Performs login action."""
        self.enter_email(email).enter_password(password).click(
            self.CONTINUE_BUTTON
        )
        return HomePage(self.driver)
