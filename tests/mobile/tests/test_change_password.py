import pytest
from ..helper import User
from ..pages.screens.settings.settings_page import SettingsPage
from ..pages.screens.home_page import HomePage


@pytest.mark.auth(user="new_user", register=True)
def test_change_password_to_new(
    settings_page: SettingsPage, new_user: User, new_password: str
):
    password_page = settings_page.navigate_to_change_password()
    password_page.change_password(new_user.password, new_password, new_password)
    password_page.wait_for_toast_to_appear(password_page.SUCCESS_TOAST_TEXT)


@pytest.mark.auth(user="updated_user", register=False)
def test_login_with_new_password(home_page: HomePage):
    pass


def test_change_password_to_old(settings_page: SettingsPage, old_user: User):
    password_page = settings_page.navigate_to_change_password()
    password_page.change_password(
        old_user.password, old_user.password, old_user.password
    )
    password_page.wait_for_toast_to_appear(
        password_page.FAILURE_TOAST_OLD_NEW_SAME_TEXT
    )


def test_change_password_wrong_confirm_new(
    settings_page: SettingsPage, old_user: User, new_password: str
):
    password_page = settings_page.navigate_to_change_password()
    password_page.change_password(
        old_user.password, new_password, new_password[:-1]
    )
    password_page.wait_for_element(
        password_page.NEW_DONT_MATCH_TEXT
    )


def test_change_password_old_not_matching(
    settings_page: SettingsPage, old_user: User, new_password: str
):
    password_page = settings_page.navigate_to_change_password()
    password_page.change_password(
        old_user.password[:-1], new_password, new_password
    )

    password_page.wait_for_toast_to_appear(
        password_page.FAILURE_TOAST_INCORRECT_OLD_TEXT
    )
