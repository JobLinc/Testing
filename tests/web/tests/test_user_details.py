from playwright.sync_api import Page, expect
from ..pages.user_details_page import UserDetailsPage
from ..config import NEW_USER
from ..config import (
    SIGNIN_EMAIL,
    SIGNIN_PASSWORD,
    INVALID_EMAIL,
    INVALID_PASSWORD,
    FIRST_NAME,
    LAST_NAME,
)


def test_valid_user_details(page: Page) -> None:

    user_details_page = UserDetailsPage(page)
    user_details_page.user_details_input(
        NEW_USER["email"], NEW_USER["password"], FIRST_NAME, LAST_NAME
    )
    expect(
        page.get_by_role("heading", name="Welcome to the Main Page"),
        "Welcome to the Main Page",
    ).to_be_visible()


def test_invalid_user_details(page: Page) -> None:

    user_details_page = UserDetailsPage(page)
    user_details_page.user_details_input(
        SIGNIN_EMAIL, SIGNIN_PASSWORD, FIRST_NAME, LAST_NAME
    )
    expect(
        page.get_by_role("heading", name="This email is already registered."),
        "This email is already registered.",
    ).to_be_visible()
