import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("WEB_BASE_URL", "https://joblinc.me")
EMAIL = os.getenv("EMAIL", "email")
PASSWORD = os.getenv("PASSWORD", "password")

BROWSERS = ["chromium", "firefox", "webkit"]
HEADLESS = True
