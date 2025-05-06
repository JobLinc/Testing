from playwright.sync_api import Page
from .base_page import BasePage
from ..pages.login_page import LoginPage
import re
from ..config import (
    LOGIN_FNAME,
    LOGIN_LNAME,
    NEWPOST,
    COMMENT,
)


def get_user_id(page: Page) -> str:
    user_id = page.url.split("/profile/")[-1]
    return user_id


def comment(page: Page):
    page.locator("div:nth-child(4) > button").first.click()
    page.get_by_role("textbox", name="Write a comment...").fill(f"{COMMENT}")
    page.get_by_role("button", name="send", exact=True).nth(1).click()
    page.wait_for_timeout(10000)
