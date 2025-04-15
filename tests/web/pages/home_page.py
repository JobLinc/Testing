from playwright.sync_api import Page
from .base_page import BasePage
from ..pages.login_page import LoginPage


class HomePage(BasePage):

    def __init__(self, page: Page, start_page: str = "https://joblinc.me/Home"):
        super().__init__(page, start_page)
        self.first_page = LoginPage(
            page, start_page="https://joblinc.me/Signin"
        )
        self.home_btn = page.get_by_role("link", name="Home")
        self.network_btn = page.get_by_role("link", name="My Network")
        self.jobs_btn = page.get_by_role("link", name="Jobs")
        self.messages_btn = 'a[href="/messaging"]'
        self.notifications_btn = page.get_by_role("link", name="Notifications")
        self.profile_btn = page.get_by_role("link", name=" Me ")
        self.business_btn = page.get_by_role("link", name="Businesses")

    def goToMessages(self, signin_email, signin_password) -> None:
        self.first_page.login(signin_email, signin_password)
        self.page.click(self.messages_btn)

    def goToProfile(self, signin_email, signin_password) -> None:
        self.first_page.login(signin_email, signin_password)
        self.profile_btn.click()
