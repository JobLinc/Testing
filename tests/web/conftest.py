import pytest
from pytest import FixtureRequest
from typing import Generator
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext
from .config import HEADLESS, BROWSERS, LOGIN_EMAIL, LOGIN_PASSWORD


from .pages.login_page import LoginPage


@pytest.fixture(params=BROWSERS)
def page(request: FixtureRequest) -> Generator[Page, None, None]:
    """Fixture to provide a Playwright page object for each browser."""
    with sync_playwright() as p:
        browser: Browser = getattr(p, request.param).launch(headless=HEADLESS)
        context: BrowserContext = browser.new_context()
        page: Page = context.new_page()

        yield page

        page.close()
        browser.close()


@pytest.fixture
def loginFixture(page: Page) -> Page:
    # Perform login steps here
    page.goto("https://joblinc.me/Signin")
    page.fill("input[name='email']", f"{LOGIN_EMAIL}")
    page.fill("input[name='password']", f"{LOGIN_PASSWORD}")
    signin_button = page.get_by_role("button", name="Sign in")
    signin_button.click()
    print("Login successful")
    print(page.url)
    return page


@pytest.fixture
def profileFixture(page: Page, loginFixture) -> Page:
    """Fixture to navigate to the home page."""
    page = loginFixture
    profile_btn = page.get_by_role("link", name=" Me ")
    profile_btn.click()
    return page


"""
@pytest.fixture(scope="function")
def loginFixture(page: Page) -> Generator[Page, None, None]:
    Fixture to log in to the application.
    login_page = LoginPage(page)
    login_page.login("login-testing@gmail.com", "login-testing")
    print("fixtrue")
    print(page.url)
    print(login_page)
    yield login_page
    """


@pytest.fixture(scope="function")
def changeEmailFixture(page: Page) -> Generator[Page, None, None]:
    """Fixture to change email."""
    page.goto("https://joblinc.me/ChangeEmail")
    page.get_by_role("textbox", name="Email").fill("email")
    page.get_by_role("button", name="Change Email").click()
    page.get_by_role("button", name="Confirm").click()
    yield page
    # return to the original email
