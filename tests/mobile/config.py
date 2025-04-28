import os
from dotenv import load_dotenv

from appium.options.android import UiAutomator2Options

load_dotenv()

APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
MAIN_APP_ACTIVITY = os.getenv(
    "MAIN_APP_ACTIVITY", "com.example.joblinc.MainActivity"
)

CAPABILITIES = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "app": os.getenv("APPIUM_APK_PATH"),
    "appWaitActivity": MAIN_APP_ACTIVITY,
}


capabilities_options = UiAutomator2Options().load_capabilities(CAPABILITIES)


"""
{
  "platformName": "Android",
  "appium:deviceName": "emulator-5554",
  "appium:automationName": "UiAutomator2",
  "appium:app": "/Users/Mo/Documents/computing/projects/Testing/Cross-Platform/build/app/outputs/apk/debug/app-x86_64-debug.apk",
  "appium:appWaitActivity": "com.example.joblinc.MainActivity"
}
"""
