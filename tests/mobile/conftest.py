import os
import pytest
import logging
from appium import webdriver

from .adb_utils import start_emulator
from .pages.screens.home_page import HomePage
from .pages.screens.auth.landing_page import LandingPage
from .config import capabilities_options, APPIUM_SERVER_URL, USER

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def emulator_setup():
    """Ensure emulator is running for all tests"""
    start_emulator()


@pytest.fixture
def app_driver():
    """Session-scoped Appium driver"""
    driver = None
    try:
        logger.info("Initializing Appium driver")
        driver = webdriver.Remote(
            command_executor=APPIUM_SERVER_URL, options=capabilities_options
        )
        driver.implicitly_wait(5)
        yield driver
    finally:
        if driver:
            logger.info("Tearing down Appium driver")
            driver.quit()


@pytest.fixture
def landing_page(app_driver):
    """Landing page fixture for non-authenticated tests"""
    page = LandingPage(app_driver)
    page.verify_page_loaded()
    return page


@pytest.fixture
def logged_in_driver(app_driver):
    """Authenticated driver fixture"""
    logger.info("Performing login workflow")
    LandingPage(app_driver).go_to_login().login(USER["email"], USER["password"])
    return app_driver


@pytest.fixture
def home_page(logged_in_driver):
    """Pre-authenticated home page"""
    page = HomePage(logged_in_driver)
    return page


@pytest.fixture
def settings_page(home_page):
    """Settings page accessed via sidebar"""
    return home_page.sidebar.navigate_to_settings()


@pytest.fixture
def register_page(landing_page):
    """Registration test context with clean state"""
    return landing_page.go_to_register()


@pytest.fixture
def login_page(landing_page):
    """Registration test context with clean state"""
    return landing_page.go_to_login()


def pytest_exception_interact(node, call, report):
    """Take screenshot on test failure"""
    driver = None
    for fixture in node.fixturenames:
        if "driver" in fixture:
            driver = node.funcargs.get(fixture)
            break

    if driver and report.failed:
        screenshot_name = os.path.join(
            "reports", "screenshots", f"FAIL_{node.name}.png"
        )

        try:
            driver.save_screenshot(screenshot_name)
            logger.info(f"Screenshot saved: {screenshot_name}")
        except Exception as e:
            logger.error(f"Failed to capture screenshot: {str(e)}")
