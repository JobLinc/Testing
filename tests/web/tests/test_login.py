from playwright.sync_api import Page, expect
from ..pages.login_page import LoginPage
from ..config import (
    SIGNIN_EMAIL,
    SIGNIN_PASSWORD,
    INVALID_EMAIL,
    INVALID_PASSWORD,
    EMAIL_DOESNT_EXIT,
)


def test_valid_login(page: Page) -> None:

    login_page = LoginPage(page)
    login_page.login(SIGNIN_EMAIL, SIGNIN_PASSWORD)
    expect(
        page.get_by_role("heading", name="Welcome to the Main Page"),
        "Welcome to the Main Page",
    ).to_be_visible()


def test_invalid_login(page: Page) -> None:

    login_page = LoginPage(page)
    login_page.login(INVALID_EMAIL, INVALID_PASSWORD)
    expect(
        page.locator("text=Please enter a valid email address")
    ).to_be_visible()

    # ERROR 1
    # expect(page.locator("text=The password must have at least 6 characters.")).to_be_visible()


def test_invalid_password(page: Page) -> None:

    login_page = LoginPage(page)
    login_page.login(SIGNIN_EMAIL, INVALID_PASSWORD)
    expect(
        page.locator("text=The password must have at least 6 characters.")
    ).to_be_visible()


def test_invalid_email(page: Page) -> None:

    login_page = LoginPage(page)
    login_page.login(INVALID_EMAIL, SIGNIN_PASSWORD)
    expect(
        page.locator("text=Please enter a valid email address")
    ).to_be_visible()


def test_email_doesnt_exist(page: Page) -> None:

    login_page = LoginPage(page)
    login_page.login(EMAIL_DOESNT_EXIT, SIGNIN_PASSWORD)
    expect(
        page.get_by_role("heading", name="Wrong Email or Password"),
        "Wrong Email or Password",
    ).to_be_visible()
