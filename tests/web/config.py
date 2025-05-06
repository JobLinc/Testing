import os
from dotenv import load_dotenv
import string
import random
import pytest
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
IMAGE1_PATH = PROJECT_ROOT / "file1.png"
IMAGE2_PATH = PROJECT_ROOT / "file2.png"


load_dotenv()


BASE_URL = os.getenv("WEB_BASE_URL", "https://joblinc.me")
EMAIL = os.getenv("EMAIL", "email")
PASSWORD = os.getenv("PASSWORD", "password")

SIGNIN_EMAIL_CHROME = os.getenv(
    "SIGNIN_EMAIL_CHROME", "testing-chrome@gmail.com"
)
SIGNIN_PASSWORD_CHROME = os.getenv(
    "SIGNIN_PASSWORD_CHROME", "first-testing-change8"
)
CHANGE_PASSWORD_CHROME = os.getenv(
    "CHANGE_PASSWORD_CHROME", "first-testing-change9"
)


SIGNIN_EMAIL_FIREFOX = os.getenv(
    "SIGNIN_EMAIL_FIREFOX", "first-testingf@gmail.com"
)
SIGNIN_PASSWORD_FIREFOX = os.getenv(
    "SIGNIN_PASSWORD_FIREFOX", "first-testing-change7"
)
CHANGE_PASSWORD_FIREFOX = os.getenv(
    "CHANGE_PASSWORD_FIREFOX", "first-testing-change8"
)

SIGNIN_EMAIL_WEBKIT = os.getenv(
    "SIGNIN_EMAIL_WEBKIT", "first-testingw@gmail.com"
)
SIGNIN_PASSWORD_WEBKIT = os.getenv(
    "SIGNIN_PASSWORD_WEBKIT", "first-testing-change8"
)
CHANGE_PASSWORD_WEBKIT = os.getenv(
    "CHANGE_PASSWORD_WEBKIT", "first-testing-change9"
)

LOGIN_EMAIL = os.getenv("LOGIN_EMAIL", "last3@email.com")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD", "last123")
LOGIN_FNAME = os.getenv("LOGIN_FNAME", "User")
LOGIN_LNAME = os.getenv("LOGIN_LNAME", "New")

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
    "headline": "Software Engineer",
    "phone": "1234567890",
}
EXPERIENCE = {
    "title": "Software Engineer",
    "company": "Tech Company",
    "start_month": 4,
    "start_year": 2020,
    "end_month": 10,
    "end_year": 2023,
    "description": "Worked on various projects",
}
SKILL = {
    "name": "Python",
    "level": 3,
}
CERTIFICATE = {
    "name": "Certificate Name",
    "organization": "Organization Name",
    "start_month": 1,
    "start_year": 2020,
    "end_month": 9,
    "end_year": 2023,
}
COMMENT = os.getenv("COMMENT", "This is a test comment")
NEWPOST = os.getenv("NEWPOST", "I am testing the posts section")
REPLY = os.getenv("REPLY", "This is a reply")

OLDEMAIL = os.getenv("OLDEMAIL", "email4@email.com")
NEWEMAIL = os.getenv("NEWEMAIL", "email5@email.com")
WEBEMAIL = os.getenv("WEBEMAIL", "email6@email.com")

BROWSERS = ["chromium", "webkit"]
HEADLESS = False
