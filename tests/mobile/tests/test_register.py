from ..config import USER, NEW_USER
from ..pages.screens.auth.register_page import RegisterPage


def test_register_valid(register_page: RegisterPage) -> None:
    """Tests a valid reigster scenario."""
    register_page.register(**NEW_USER)


def test_register_email_already_exists(register_page: RegisterPage) -> None:
    """Tests a valid reigster scenario."""
    register_page.enter_first_last_name(USER["first_name"], USER["last_name"])
    register_page.enter_email_password(USER["email"], USER["password"])
    register_page.enter_country_city_phone(USER["country"], USER["city"])
    register_page.wait_for_toast_to_appear(register_page.ERROR_TOAST)


def test_register_empty_first_name(register_page: RegisterPage) -> None:
    register_page.enter_first_last_name("", USER["last_name"])
    register_page.wait_for_element(register_page.EMPTY_FIRST_NAME_TEXT)


def test_register_empty_last_name(register_page: RegisterPage) -> None:
    register_page.enter_first_last_name(USER["first_name"], "")
    register_page.wait_for_element(register_page.EMPTY_LAST_NAME_TEXT)


def test_register_empty_email(register_page: RegisterPage) -> None:
    register_page.enter_first_last_name(USER["first_name"], USER["last_name"])
    register_page.enter_email_password("", USER["password"])
    register_page.wait_for_element(register_page.EMPTY_EMAIL_TEXT)


def test_register_empty_password(register_page: RegisterPage) -> None:
    register_page.enter_first_last_name(
        USER["first_name"], USER["last_name"]
    ).enter_email_password(USER["email"], "")
    register_page.wait_for_element(register_page.EMPTY_PASSWORD_TEXT)


def test_register_empty_country(register_page: RegisterPage) -> None:
    register_page.enter_first_last_name(USER["first_name"], USER["last_name"])
    register_page.enter_email_password(USER["email"], USER["password"])
    register_page.enter_country_city_phone("", USER["city"])
    register_page.wait_for_element(register_page.EMPTY_COUNTRY_TEXT)


def test_register_empty_city(register_page: RegisterPage) -> None:
    register_page.enter_first_last_name(USER["first_name"], USER["last_name"])
    register_page.enter_email_password(USER["email"], USER["password"])
    register_page.enter_country_city_phone(USER["country"], "")
    register_page.wait_for_element(register_page.EMPTY_CITY_TEXT)
