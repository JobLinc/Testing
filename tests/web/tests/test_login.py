from playwright.sync_api import Page
from ..pages.login_page import LoginPage
from ..config import EMAIL, PASSWORD


def test_valid_login(page: Page) -> None:
    # TODO: This is just an example function
    login_page = LoginPage(page)
    login_page.login(EMAIL, PASSWORD)
    assert page.url == "https://joblinc.me/UserDetails"
