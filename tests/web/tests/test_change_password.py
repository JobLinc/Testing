from playwright.sync_api import Page, expect
from ..pages.change_password_page import ChangePasswordPage
from ..pages.login_page import LoginPage
from ..config import (
    SIGNIN_EMAIL,
    SIGNIN_PASSWORD,
    CHANGE_PASSWORD,
    INCORRECT_PASSWORD,
)


def test_valid_change_password(page: Page) -> None:
    change_password_Page = ChangePasswordPage(page)
    change_password_Page.changePassword(
        SIGNIN_EMAIL, SIGNIN_PASSWORD, SIGNIN_PASSWORD, CHANGE_PASSWORD
    )
    expect(
        page.get_by_role("heading", name="Password Changed Successfully"),
        "Password Changed Successfully",
    ).to_be_visible()
    login_page = LoginPage(page)
    login_page.login(SIGNIN_EMAIL, CHANGE_PASSWORD)
    expect(
        page.get_by_role("heading", name="Welcome to the Main Page"),
        "Welcome to the Main Page",
    ).to_be_visible()


def test_invalid_change_password_incorrect_old_password(page: Page) -> None:
    change_password_Page = ChangePasswordPage(page)
    change_password_Page.changePassword(
        SIGNIN_EMAIL, CHANGE_PASSWORD, INCORRECT_PASSWORD, SIGNIN_PASSWORD
    )
    expect(
        page.get_by_role("heading", name="Old password is incorrect"),
        "Old password is incorrect",
    ).to_be_visible()


def test_invalid_change_password_same_old_and_new_password(page: Page) -> None:
    change_password_Page = ChangePasswordPage(page)
    change_password_Page.changePassword(
        SIGNIN_EMAIL, CHANGE_PASSWORD, SIGNIN_PASSWORD, SIGNIN_PASSWORD
    )
    expect(
        page.locator("text=New password can't be as old password.")
    ).to_be_visible()
