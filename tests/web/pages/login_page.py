from playwright.sync_api import Page
from .base_page import BasePage


class LoginPage(BasePage):

    def __init__(
        self, page: Page, start_page: str = "https://joblinc.me/Signup"
    ):
        super().__init__(page, start_page)
        self.email_input = "input[name='email']"
        self.password_input = "input[name='password']"
        self.login_button = "#root > div > div > form > div.flex.w-full.flex-col.items-center.justify-center > button"

    def login(self, email: str, password: str) -> None:
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
