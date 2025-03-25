from playwright.sync_api import Page
from .base_page import BasePage


class SignupPage(BasePage):

    def __init__(
        self, page: Page, start_page: str = "https://joblinc.me/Signup"
    ):
        super().__init__(page, start_page)
        self.email_input = "input[name='email']"
        self.password_input = "input[name='password']"
        self.signup_button = page.get_by_role("button", name="Agree & Join")

    def signup(self, email: str, password: str) -> None:
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        self.signup_button.click()
        # self.page.wait_for_url("**/UserDetails", timeout=10000)
