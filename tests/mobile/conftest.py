import pytest
from appium import webdriver
from .adb_utils import start_emulator
from .config import capabilities_options, APPIUM_SERVER_URL


@pytest.fixture(scope="session", autouse=True)
def ensure_emulator():
    """Ensure the emulator is running before any test runs."""
    start_emulator()


@pytest.fixture(scope="function")
def driver():
    """Sets up an Appium driver for each test."""
    driver = webdriver.Remote(APPIUM_SERVER_URL, options=capabilities_options)
    yield driver
    driver.quit()
