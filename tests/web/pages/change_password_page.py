from playwright.sync_api import Page
from .base_page import BasePage
from ..pages.login_page import LoginPage


class ChangePasswordPage(BasePage):

    def __init__(
        self, page: Page, start_page: str = "https://joblinc.me/ChangePassword"
    ):
        super().__init__(page, start_page)
        self.first_page = LoginPage(
            page, start_page="https://joblinc.me/Signin"
        )
        self.change_password = page.get_by_role("link", name="Change password")
        self.old_password_input = page.locator(
            'input[type="password"][required]'
        ).nth(0)
        self.new_password_input = page.locator(
            'input[type="password"][required]'
        ).nth(1)
        self.done_button = page.get_by_role(" button", name="Done")

    def changePassword(
        self,
        signin_email: str,
        signin_password: str,
        old_password: str,
        new_password: str,
    ) -> None:

        self.first_page.login(signin_email, signin_password)
        self.change_password.click()
        self.old_password_input.fill(old_password)
        self.new_password_input.fill(new_password)
        self.done_button.click()
