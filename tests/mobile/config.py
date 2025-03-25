import os
import string
import random
from dotenv import load_dotenv

from appium.options.android import UiAutomator2Options

load_dotenv()

APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")

CAPABILITIES = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "app": os.getenv("APPIUM_APK_PATH"),
    "appWaitActivity": os.getenv(
        "MAIN_APP_ACTIVITY", "com.example.joblinc.MainActivity"
    ),
}

NEW_USER = {
    "first_name": "test_firstname",
    "last_name": "test_lastname",
    "email": "".join(random.choice(string.ascii_letters) for _ in range(10))
    + "@email.com",
    "password": "password",
    "country": "Egypt",
    "city": "6th of October",
}

USER = {
    "first_name": os.getenv("FIRST_NAME", "first1"),
    "last_name": os.getenv("LAST_NAME", "last1"),
    "email": os.getenv("EMAIL", "email1"),
    "password": os.getenv("PASSWORD", "password1"),
    "country": "Egypt",
    "city": "6th of October",
}

capabilities_options = UiAutomator2Options().load_capabilities(CAPABILITIES)
