import os
from dotenv import load_dotenv
import string
import random

load_dotenv()

BASE_URL = os.getenv("WEB_BASE_URL", "https://joblinc.me")
EMAIL = os.getenv("EMAIL", "email")
PASSWORD = os.getenv("PASSWORD", "password")

SIGNIN_EMAIL = os.getenv("SIGNIN_EMAIL", "first-testing@gmail.com")
SIGNIN_PASSWORD = os.getenv("SIGNIN_PASSWORD", "first-testing-change")
CHANGE_PASSWORD = os.getenv("CHANGE_PASSWORD", "first-testing-change1")

INCORRECT_PASSWORD = os.getenv("INCORRECT_PASSWORD", "incorrect-password-123")

INVALID_EMAIL = os.getenv("INVALID_EMAIL", "wrong-testing@gmail")
INVALID_PASSWORD = os.getenv("INVALID_PASSWORD", "123")
EMAIL_DOESNT_EXIT = os.getenv(
    "EMAIL_DOESNT_EXIT", "first-testing-not-found@gmail.com"
)


SIGNUP_EMAIL = os.getenv("SIGNUP_EMAIL", "second-testing@gmail.com")
SIGNUP_PASSWORD = os.getenv("SIGNUP_PASSWORD", "second-testing-update")

FIRST_NAME = os.getenv("FIRST_NAME", "firstname")
LAST_NAME = os.getenv("LAST_NAME", "lastname")
PHONE = os.getenv("PHONE", "1234567890")

INVALID_FNAME = os.getenv("INVALID_FNAME", "123")
INVALID_LNAME = os.getenv("INVALID_LNAME", "123")


NEW_USER = {
    "first_name": "test_firstname",
    "last_name": "test_lastname",
    "email": "".join(random.choice(string.ascii_letters) for _ in range(10))
    + "@email.com",
    "password": "password",
    "country": "Egypt",
    "city": "6th of October",
}

COMMENT = os.getenv("COMMENT", "This is a test comment")

BROWSERS = ["chromium"]
HEADLESS = False
