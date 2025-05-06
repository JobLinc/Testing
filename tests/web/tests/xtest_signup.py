from playwright.sync_api import Page, expect
from ..pages.signup_page import SignupPage
from ..config import (
    SIGNUP_EMAIL,
    SIGNUP_PASSWORD,
    INVALID_EMAIL,
    INVALID_PASSWORD,
)


def test_valid_signup(page: Page) -> None:
    signup_page = SignupPage(page)
    signup_page.signup(SIGNUP_EMAIL, SIGNUP_PASSWORD)
    expect(
        page.locator("text=Make the most of your professional life")
    ).to_be_visible()


def test_invalid_signup_email(page: Page) -> None:
    signup_page = SignupPage(page)
    signup_page.signup(INVALID_EMAIL, SIGNUP_PASSWORD)
    expect(
        page.locator("text=Please enter a valid email address")
    ).to_be_visible()


def test_invalid_signup_password(page: Page) -> None:
    signup_page = SignupPage(page)
    signup_page.signup(SIGNUP_EMAIL, INVALID_PASSWORD)
    expect(
        page.locator("text=Password must be 6 characters or more.")
    ).to_be_visible()


def test_invalid_signup_email_password(page: Page) -> None:
    login_page = SignupPage(page)
    login_page.signup(INVALID_EMAIL, INVALID_PASSWORD)
    expect(
        page.locator("text=Password must be 6 characters or more.")
    ).to_be_visible()
    expect(
        page.locator("text=Please enter a valid email address")
    ).to_be_visible()
