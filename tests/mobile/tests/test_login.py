from ..helper import User
from ..pages.screens.auth.login_page import LoginPage
from ..pages.screens.settings.settings_page import SettingsPage


def test_login_valid(login_page: LoginPage, old_user: User) -> None:
    """Tests a valid login scenario."""
    login_page.login(old_user.email, old_user.password)


def test_login_invalid(login_page: LoginPage, new_user: User) -> None:
    """Tests a invalid login scenario."""
    login_page.enter_email(new_user.email)
    login_page.enter_password(new_user.password)
    login_page.click(login_page.CONTINUE_BUTTON)
    login_page.wait_for_toast_to_appear(login_page.FAILURE_TOAST_TEXT)


def test_login_empty_email(login_page: LoginPage, new_user: User) -> None:
    """Tests logging in with no email."""
    login_page.enter_password(new_user.password)
    login_page.click(login_page.CONTINUE_BUTTON)
    login_page.wait_for_element(login_page.EMPTY_EMAIL_TEXT)


def test_login_empty_password(login_page: LoginPage, new_user: User) -> None:
    """Tests logging in with no password."""
    login_page.enter_email(new_user.email)
    login_page.click(login_page.CONTINUE_BUTTON)
    login_page.wait_for_element(login_page.EMPTY_PASSWORD_TEXT)


def test_successful_logout(settings_page: SettingsPage) -> None:
    """Tests logging out."""
    settings_page.logout()
