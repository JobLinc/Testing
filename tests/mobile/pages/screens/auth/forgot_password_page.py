from typing import Self
from appium.webdriver.common.appiumby import AppiumBy
from ...base_page import BasePage
from ..auth.login_page import LoginPage


class ForgotPasswordPage(BasePage):
    """Page object for the Forgot Password screen."""

    HEADING = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Forgot Password")',
    )

    INPUT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText")',
    )

    CONTINUE_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Continue")',
    )

    PASSWORD_STAGE_IDENTIFIER_TOAST_TEXT = "OTP verified successfully"
    OTP_STAGE_IDENTIFIER_TOAST_TEXT = "OTP sent to your email"

    # when the @ symbol is not present
    FAILURE_INVALID_EMAIL_TOAST_TEXT = "Invalid email"

    # when the otp or email is invalid
    FAILURE_INVALID_OTP_OR_EMAIL_TOAST_TEXT = "Invalid OTP"

    # when the email field is empty
    FAILURE_EMAIL_REQUIRED_TOAST_TEXT = "Email is required"

    # when the otp field is empty
    FAILURE_OTP_REQUIRED_TOAST_TEXT = "OTP is required"

    # when the new password field is empty
    FAILURE_NEW_PASSWORD_REQUIRED_TOAST_TEXT = "New password is required"

    def verify_page_loaded(self, timeout=15) -> None:
        self.wait_for_element(self.HEADING, timeout)

    def enter_email(self, email: str) -> Self:
        self.enter_text(self.INPUT, email)
        self.click(self.CONTINUE_BUTTON)
        return self

    def enter_otp(self, otp: str) -> Self:
        self.wait_for_toast_to_appear(self.OTP_STAGE_IDENTIFIER_TOAST_TEXT)
        self.enter_text(self.INPUT, otp)
        self.click(self.CONTINUE_BUTTON)
        return self

    def enter_reset_password(self, new_password: str) -> Self:
        self.wait_for_toast_to_appear(self.PASSWORD_STAGE_IDENTIFIER_TOAST_TEXT)
        self.enter_text(self.INPUT, new_password)
        self.click(self.CONTINUE_BUTTON)
        return self

    def reset_password(
        self, email: str, otp: str, new_password: str
    ) -> LoginPage:

        self.enter_email(email)
        self.enter_otp(otp)
        self.enter_reset_password(new_password)
        return LoginPage(self.driver)
