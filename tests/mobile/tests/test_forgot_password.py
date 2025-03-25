import pytest

from ..helper import User
from ..pages.screens.auth.login_page import LoginPage
from ..pages.screens.settings.settings_page import SettingsPage


def test_forgot_password_malformed_email(login_page: LoginPage) -> None:
    forgot_password_page = login_page.navigate_to_forgot_password_page()
    forgot_password_page.enter_email("email")
    forgot_password_page.wait_for_toast_to_appear(
        forgot_password_page.FAILURE_INVALID_EMAIL_TOAST_TEXT
    )


def test_forgot_password_empty_email(login_page: LoginPage) -> None:
    forgot_password_page = login_page.navigate_to_forgot_password_page()
    forgot_password_page.enter_email("")
    forgot_password_page.wait_for_toast_to_appear(
        forgot_password_page.FAILURE_EMAIL_REQUIRED_TOAST_TEXT
    )


def test_forgot_password_invalid_email(
    login_page: LoginPage, new_user: User
) -> None:
    forgot_password_page = login_page.navigate_to_forgot_password_page()
    forgot_password_page.enter_email(new_user.email)
    forgot_password_page.enter_otp("123456")
    forgot_password_page.wait_for_toast_to_appear(
        forgot_password_page.FAILURE_INVALID_OTP_OR_EMAIL_TOAST_TEXT
    )


def test_forgot_password_empty_otp(
    login_page: LoginPage, old_user: User
) -> None:
    forgot_password_page = login_page.navigate_to_forgot_password_page()
    forgot_password_page.enter_email(old_user.email).enter_otp("")
    forgot_password_page.wait_for_toast_to_appear(
        forgot_password_page.FAILURE_OTP_REQUIRED_TOAST_TEXT
    )


def test_forgot_password_invalid_otp(
    login_page: LoginPage, old_user: User
) -> None:
    forgot_password_page = login_page.navigate_to_forgot_password_page()
    forgot_password_page.enter_email(old_user.email)
    forgot_password_page.enter_otp("000000")
    forgot_password_page.wait_for_toast_to_appear(
        forgot_password_page.FAILURE_INVALID_OTP_OR_EMAIL_TOAST_TEXT
    )


# def test_forgot_password_empty_new_password(
#     login_page: LoginPage, old_user: User
# ) -> None:
#     forgot_password_page = login_page.navigate_to_forgot_password_page()
#     forgot_password_page.enter_email(old_user.email)
#     forgot_password_page.enter_otp("123456")
#     forgot_password_page.enter_reset_password("")
#     forgot_password_page.wait_for_toast_to_appear(
#         forgot_password_page.FAILURE_NEW_PASSWORD_REQUIRED_TOAST_TEXT
#     )


@pytest.mark.auth(user="new_user", register=True)
def test_valid_reset_password(settings_page: SettingsPage, new_user: User):
    login_page = settings_page.logout()
    forgot_password_page = login_page.navigate_to_forgot_password_page()
    forgot_password_page.reset_password(
        new_user.email, "123456", new_user.password
    )
