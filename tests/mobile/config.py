import os
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
    "noReset": True,
}

EMAIL = os.getenv("EMAIL", "email")
PASSWORD = os.getenv("PASSWORD", "password")

capabilities_options = UiAutomator2Options().load_capabilities(CAPABILITIES)
