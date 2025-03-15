from ..pages.login_page import LoginPage
from ..config import EMAIL, PASSWORD


def test_valid_login(driver):
    """Tests a valid login scenario."""
    login_page = LoginPage(driver)
    login_page.login(EMAIL, PASSWORD)

    assert "Tyrone" in driver.page_source, "Login failed!"
