from appium.webdriver.common.appiumby import AppiumBy
from ...base_page import BasePage
from ..home_page import HomePage


class RegisterPage(BasePage):
    """Page object for the register screen."""

    # Input fields
    FIRST_NAME_INPUT = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Step 1 of 3"]/android.widget.EditText[1]',
    )
    LAST_NAME_INPUT = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Step 1 of 3"]/android.widget.EditText[2]',
    )
    EMAIL_INPUT = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Step 2 of 3"]/android.widget.EditText[1]',
    )
    PASSWORD_INPUT = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="Step 2 of 3"]/android.widget.EditText[2]',
    )
    COUNTRY_CHOICE = (
        AppiumBy.XPATH,
        "//android.widget.Button[@content-desc='Country\nEgypt']",
    )

    CITY_CHOICE = (
        AppiumBy.XPATH,
        "//android.widget.Button[@content-desc='City']",
    )

    PHONE_NUMBER_INPUT = (
        AppiumBy.XPATH,
        "//android.widget.EditText[@hint='Phone Number (Optional)']",
    )

    # Buttons
    CONTINUE_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Continue")',
    )
    SUBMIT_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Submit")',
    )

    # Validation error messages
    EMPTY_FIRST_NAME_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Please enter your first name")',
    )
    EMPTY_LAST_NAME_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Please enter your last name")',
    )
    EMPTY_EMAIL_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Please enter your email")',
    )
    EMPTY_PASSWORD_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Please enter your password")',
    )

    EMPTY_CITY_TEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Please select your city")',
    )

    OTP_INPUT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText")',
    )

    OTP_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Verify Code")

    # Toast messages
    SUCCESS_TOAST = "Registration Successful"
    ERROR_TOAST = "Email already exists"

    def verify_page_loaded(self, timeout: int = 15) -> None:
        """Ensures the register screen is loaded by checking the first name input field."""
        self.wait_for_element(self.FIRST_NAME_INPUT, timeout)

    def enter_first_last_name(self, first_name: str, last_name: str):
        """Fills in the first and last name and proceeds to the next step."""
        return (
            self.enter_text(self.FIRST_NAME_INPUT, first_name)
            .enter_text(self.LAST_NAME_INPUT, last_name)
            .click(self.CONTINUE_BUTTON)
        )

    def enter_email_password(self, email: str, password: str):
        """Fills in the email and password and proceeds to the next step."""
        return (
            self.enter_text(self.EMAIL_INPUT, email)
            .enter_text(self.PASSWORD_INPUT, password)
            .click(self.CONTINUE_BUTTON)
        )

    def enter_country_city_phone(
        self, country: str, city: str, phone_number: str = ""
    ):
        """Fills in country, city, and optional phone number, then submits the form."""
        if country:
            self.choose_dropdown(self.COUNTRY_CHOICE, country)

        if city:
            self.choose_dropdown(self.CITY_CHOICE, city)

        if phone_number:
            self.enter_text(self.PHONE_NUMBER_INPUT, phone_number)
        return self.click(self.SUBMIT_BUTTON)

    def enter_otp(self) -> None:
        self.enter_text(self.OTP_INPUT, "123456")
        self.click(self.OTP_BUTTON)

    def register(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        country: str,
        city: str,
        phone_number: str = "",
    ):
        """Performs the full registration process."""
        self.enter_first_last_name(first_name, last_name).enter_email_password(
            email, password
        ).enter_country_city_phone(country, city, phone_number)

        self.enter_otp()

        return HomePage(self.driver)
