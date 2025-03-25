import pytest
from ..pages.base_page import PageNavigationError
from ..config import USER, NEW_USER
from ..pages.screens.auth.login_page import LoginPage
from ..pages.screens.settings.settings_page import SettingsPage


def test_login_valid(login_page: LoginPage) -> None:
    """Tests a valid login scenario."""
    login_page.login(USER["email"], USER["password"])


def test_login_invalid(login_page: LoginPage) -> None:
    """Tests a invalid login scenario."""
    login_page.enter_email(NEW_USER["email"])
    login_page.enter_password(NEW_USER["password"])
    login_page.click(login_page.CONTINUE_BUTTON)
    login_page.wait_for_toast_to_appear(login_page.FAILURE_TOAST_TEXT)


def test_login_empty_email(login_page: LoginPage) -> None:
    """Tests logging in with no email."""
    login_page.enter_password(NEW_USER["password"])
    login_page.click(login_page.CONTINUE_BUTTON)
    login_page.wait_for_element(login_page.EMPTY_EMAIL_TEXT)


def test_login_empty_password(login_page: LoginPage) -> None:
    """Tests logging in with no password."""
    login_page.enter_email(NEW_USER["email"])
    login_page.click(login_page.CONTINUE_BUTTON)
    login_page.wait_for_element(login_page.EMPTY_PASSWORD_TEXT)


def test_successful_logout(settings_page: SettingsPage) -> None:
    """Tests logging out."""
    settings_page.logout()
