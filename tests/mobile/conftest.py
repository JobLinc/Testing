import os
import string
import random
import pytest
import logging

from appium import webdriver

from .helper import User
from .adb_utils import start_emulator
from .pages.screens.home_page import HomePage
from .pages.screens.auth.landing_page import LandingPage
from .config import capabilities_options, APPIUM_SERVER_URL

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def emulator_setup():
    """Ensure emulator is running for all tests"""
    start_emulator()


@pytest.fixture(scope="session")
def old_user():
    """Fixture for credentials to an old user"""
    first_name = os.getenv("FIRST_NAME", "first")
    last_name = os.getenv("LAST_NAME", "last")
    email = os.getenv("EMAIL", "user100@email.com")
    password = os.getenv("PASSWORD", "user101")

    return User(
        first_name,
        last_name,
        email,
        password,
        "Egypt",
        "Alexandria",
    )


@pytest.fixture(scope="module")
def new_user():
    """Fixture for credentials for a new user."""
    email = (
        "".join(random.choice(string.ascii_letters) for _ in range(10))
        + "@email.com"
    )

    return User(
        "test_firstname",
        "test_lastname",
        email,
        "password",
        "Egypt",
        "Alexandria",
    )


@pytest.fixture(scope="module")
def new_password():
    """Shared new password for tests."""
    return "new_password123"


@pytest.fixture
def updated_user(new_user, new_password):
    """Returns new_user with an updated password."""
    return User(
        new_user.first_name,
        new_user.last_name,
        new_user.email,
        new_password,
        new_user.country,
        new_user.city,
    )


@pytest.fixture
def auth_params(request, old_user):
    """Dynamically get auth parameters from test markers."""
    auth_marker = request.node.get_closest_marker("auth")
    if auth_marker:
        user = auth_marker.kwargs.get("user", old_user)
        register = auth_marker.kwargs.get("register", False)
        return {"user": request.getfixturevalue(user), "register": register}
    return {"user": old_user, "register": False}


@pytest.fixture(scope="session")
def app_driver():
    """Appium driver"""
    driver = None
    try:
        logger.info("Initializing Appium driver")
        driver = webdriver.Remote(
            command_executor=APPIUM_SERVER_URL, options=capabilities_options
        )
        yield driver
    finally:
        if driver:
            logger.info("Tearing down Appium driver")
            driver.quit()


@pytest.fixture(autouse=True)
def reset_to_landing_page(app_driver):
    """Reset to landing page before each test"""
    app_driver.terminate_app("com.example.joblinc")
    app_driver.execute_script(
        "mobile: clearApp", {"appId": "com.example.joblinc"}
    )
    app_driver.activate_app("com.example.joblinc")
    yield


@pytest.fixture
def authenticated_driver(app_driver, auth_params):
    """Authenticated driver using specified user and action (register/login)."""
    user = auth_params["user"]
    register = auth_params.get("register", False)
    landing_page = LandingPage(app_driver)
    if register:
        register_page = landing_page.go_to_register()
        register_page.register(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=user.password,
            country=user.country,
            city=user.city,
        )
    else:
        login_page = landing_page.go_to_login()
        login_page.login(user.email, user.password)
    return app_driver


@pytest.fixture
def landing_page(app_driver):
    """Landing page fixture for non-authenticated tests"""
    page = LandingPage(app_driver)
    page.verify_page_loaded()
    return page


@pytest.fixture
def register_page(landing_page):
    """Registration test context with clean state"""
    return landing_page.go_to_register()


@pytest.fixture
def login_page(landing_page):
    """Registration test context with clean state"""
    return landing_page.go_to_login()


@pytest.fixture
def home_page(authenticated_driver):
    """Pre-authenticated home page"""
    page = HomePage(authenticated_driver)
    return page


@pytest.fixture
def settings_page(home_page):
    """Settings page accessed via sidebar"""
    return home_page.sidebar.navigate_to_settings()
