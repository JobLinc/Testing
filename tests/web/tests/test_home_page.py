from playwright.sync_api import Page, expect
from ..pages.home_page import HomePage
from ..pages.login_page import LoginPage
from ..config import (
    LOGIN_FNAME,
    LOGIN_LNAME,
    LOGIN_EMAIL,
    LOGIN_PASSWORD,
    NEWPOST,
)


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


def test_new_post(page: Page, loginFixture) -> None:
    home_page = loginFixture
    # page.get_by_role("textbox", name="Write a new post...").click()
    home_page.get_by_role("textbox", name="Write a new post...").fill(
        f"{NEWPOST}"
    )
    home_page.get_by_role("button", name="send", exact=True).click()
    expect(page.get_by_text(f"{NEWPOST}").first).to_be_visible()
