from playwright.sync_api import Page
from .base_page import BasePage
from ..pages.login_page import LoginPage


class ChangeEmailPage(BasePage):

    def __init__(
        self, page: Page, start_page: str = "https://joblinc.me/ChangeEmail"
    ):
        super().__init__(page, start_page)

        # no login page
        # self.first_page = LoginPage(
        #   page, start_page="https://joblinc.me/Signin"
        # )
        self.page
        self.change_email = page.get_by_role("link", name="Change email")
        self.old_email_input = page.locator(
            'input[type="email"][required]'
        ).nth(0)
        self.new_password_input = page.locator(
            'input[type="email"][required]'
        ).nth(1)

        self.done_button = page.get_by_role(" button", name="Done")

    def changeEmail(self, old_email: str, new_email: str, loginFixture) -> None:
        # login first to go to the main page
        self.page = loginFixture
        # click the change email buttin in the main page
        self.change_email.click()

        # use the change email fixture to change email and yield the page
