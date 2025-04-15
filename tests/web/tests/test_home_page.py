from playwright.sync_api import Page, expect
from ..pages.home_page import HomePage
from ..pages.login_page import LoginPage
from ..config import LOGIN_FNAME, LOGIN_LNAME, LOGIN_EMAIL, LOGIN_PASSWORD


def test_go_to_messages(page: Page, loginFixture):
    home_page = loginFixture
    home_page.get_by_role("link", name=" Messaging").click()
    expect(
        page.get_by_role("heading", name="Messaging"),
        "Messaging",
    ).to_be_visible()


def test_go_to_network(page: Page, loginFixture):
    home_page = loginFixture
    home_page.get_by_role("link", name="My Network").click()
    expect(page.get_by_text("Manage my network")).to_be_visible()


def test_go_to_profile(page: Page, loginFixture):
    home_page = loginFixture
    home_page.get_by_role("link", name=" Me ").click()
    expect(
        page.get_by_role("heading", name=f"{LOGIN_FNAME} {LOGIN_LNAME}")
    ).to_be_visible()


"""
#not using fixtures
def test_messages(page:Page) -> None:
    home_page = HomePage(page)
   
    home_page.goToMessages(LOGIN_EMAIL, LOGIN_PASSWORD)
    expect(
        page.get_by_role("heading", name="Messaging"),
        "Messaging",
    ).to_be_visible()
    
    
def test_profile(page:Page) -> None:
    home_page = HomePage(page)
    
    home_page.goToProfile(LOGIN_EMAIL, LOGIN_PASSWORD)
    expect(
        page.get_by_role("heading" , name=f"{LOGIN_FNAME} {LOGIN_LNAME}")).to_be_visible()
        """
