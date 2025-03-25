from ..helper import User
from ..pages.screens.auth.register_page import RegisterPage


def test_register_valid(register_page: RegisterPage, new_user: User) -> None:
    """Tests a valid reigster scenario."""
    register_page.register(
        new_user.first_name,
        new_user.last_name,
        new_user.email,
        new_user.password,
        new_user.country,
        new_user.city,
    )


def test_register_email_already_exists(
    register_page: RegisterPage, old_user: User
) -> None:
    """Tests a valid reigster scenario."""
    register_page.enter_first_last_name(old_user.first_name, old_user.last_name)
    register_page.enter_email_password(old_user.email, old_user.password)
    register_page.enter_country_city_phone(old_user.country, old_user.city)
    register_page.wait_for_toast_to_appear(register_page.ERROR_TOAST)


def test_register_empty_first_name(
    register_page: RegisterPage, old_user: User
) -> None:
    register_page.enter_first_last_name("", old_user.last_name)
    register_page.wait_for_element(register_page.EMPTY_FIRST_NAME_TEXT)


def test_register_empty_last_name(
    register_page: RegisterPage, old_user: User
) -> None:
    register_page.enter_first_last_name(old_user.first_name, "")
    register_page.wait_for_element(register_page.EMPTY_LAST_NAME_TEXT)


def test_register_empty_email(
    register_page: RegisterPage, old_user: User
) -> None:
    register_page.enter_first_last_name(old_user.first_name, old_user.last_name)
    register_page.enter_email_password("", old_user.password)
    register_page.wait_for_element(register_page.EMPTY_EMAIL_TEXT)


def test_register_empty_password(
    register_page: RegisterPage, old_user: User
) -> None:
    register_page.enter_first_last_name(
        old_user.first_name, old_user.last_name
    ).enter_email_password(old_user.email, "")
    register_page.wait_for_element(register_page.EMPTY_PASSWORD_TEXT)


def test_register_empty_country(
    register_page: RegisterPage, old_user: User
) -> None:
    register_page.enter_first_last_name(old_user.first_name, old_user.last_name)
    register_page.enter_email_password(old_user.email, old_user.password)
    register_page.enter_country_city_phone("", old_user.city)
    register_page.wait_for_element(register_page.EMPTY_COUNTRY_TEXT)


def test_register_empty_city(
    register_page: RegisterPage, old_user: User
) -> None:
    register_page.enter_first_last_name(old_user.first_name, old_user.last_name)
    register_page.enter_email_password(old_user.email, old_user.password)
    register_page.enter_country_city_phone(old_user.country, "")
    register_page.wait_for_element(register_page.EMPTY_CITY_TEXT)
