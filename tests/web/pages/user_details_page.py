from playwright.sync_api import Page
from .base_page import BasePage
from ..pages.signup_page import SignupPage
from ..config import SIGNUP_EMAIL, SIGNUP_PASSWORD


class UserDetailsPage(BasePage):

    def __init__(
        self, page: Page, start_page: str = "https://joblinc.me/UserDetails"
    ):
        super().__init__(page, start_page)
        self.first_page = SignupPage(
            page, start_page="https://joblinc.me/Signup"
        )
        self.first_name_input = page.get_by_role("textbox", name="First name")
        self.last_name_input = page.get_by_role("textbox", name="Last name")
        self.continue_btn = page.locator("#continue-btn")
        self.phone_number_input = page.get_by_role(
            "textbox", name="Phone number"
        )
        self.phone_number_button = page.locator("#submit-phone-no-btn")

    def user_details_input(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        phone_number: str = "",
    ) -> None:
        self.first_page.signup(email, password)
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.continue_btn.click()

        if phone_number:
            self.phone_number_input.fill(phone_number)
        self.phone_number_button.click()
