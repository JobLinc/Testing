from playwright.sync_api import Page, expect
from ..pages.change_email_page import (
    signin_with_email,
    confirm_email,
    change_email,
)
from ..config import OLDEMAIL, NEWEMAIL, WEBEMAIL
import re


def test_change_email(page: Page):
    browser = page.context.browser
    browser_type = browser.browser_type.name

    if browser_type == "chromium":

        signin_with_email(page, NEWEMAIL)
        change_email(page, NEWEMAIL)

        expect(page).to_have_url("https://joblinc.me/Home")
        # expect(page.get_by_role("navigation")).to_be_visible()
        # page.get_by_role("link", name=" Me ").click()
        # page.get_by_role("button", name="View Profile").click()
        # expect(page.get_by_role("heading", name="email email")).to_be_visible()

    if browser_type == "webkit":
        signin_with_email(page, NEWEMAIL)
        change_email(page, OLDEMAIL)
        expect(page).to_have_url("https://joblinc.me/Home")


def test_confirm_email(page: Page):
    signin_with_email(page, OLDEMAIL)
    confirm_email(page)
