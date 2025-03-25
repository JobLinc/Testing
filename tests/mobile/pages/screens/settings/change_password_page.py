from appium.webdriver.common.appiumby import AppiumBy
from ...base_page import BasePage


class ChangePasswordPage(BasePage):
    """Page object for the change password screen."""

    OLD_PASSWORD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(0)',
    )
    NEW_PASSWORD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(1)',
    )
    CONFIRM_NEW_PASSWORD = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").instance(2)',
    )
    CHANGE_PASSWORD_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Change Password").instance(1)',
    )

    SUCCESS_TOAST_TEXT = "Password changed successfully"

    FAILURE_TOAST_OLD_NEW_SAME_TEXT = (
        "Exception: Old password and new password cannot be the same"
    )
    FAILURE_TOAST_NEW_DONT_MATCH_TEXT = "New passwords do not match"
    FAILURE_TOAST_INCORRECT_OLD_TEXT = "Exception: Unauthorized request"

    def verify_page_loaded(self, timeout: int = 5) -> None:
        """Ensure the change password page is loaded."""
        self.wait_for_element(self.OLD_PASSWORD, timeout)
        self.wait_for_element(self.NEW_PASSWORD, timeout)
        self.wait_for_element(self.CONFIRM_NEW_PASSWORD, timeout)

    def change_password(
        self, old_password: str, new_password: str, confirm_new_password: str
    ) -> BasePage:
        """Change password and return current page instance."""
        self.enter_text(self.OLD_PASSWORD, old_password)
        self.enter_text(self.NEW_PASSWORD, new_password)
        self.enter_text(self.CONFIRM_NEW_PASSWORD, confirm_new_password)
        self.click(self.CHANGE_PASSWORD_BUTTON)
        return self
