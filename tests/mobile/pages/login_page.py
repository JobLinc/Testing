from .base_page import BasePage


class LoginPage(BasePage):
    """Page object for the login screen."""

    def __init__(self, driver):
        super().__init__(driver)
        self.agree_and_join_id = "Sign in with email "
        self.email_xpath = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]'
        self.password_xpath = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]'
        self.remember_me_classname = "android.widget.CheckBox"
        self.continue_id = "Continue"

    def login(self, email: str, password: str):
        """Performs login action."""
        self.click_by_accessibility_id(self.agree_and_join_id)
        self.enter_text_by_xpath(self.email_xpath, email)
        self.enter_text_by_xpath(self.password_xpath, password)
        self.find_by_classname(self.remember_me_classname).click()
        self.click_by_accessibility_id(self.continue_id)
