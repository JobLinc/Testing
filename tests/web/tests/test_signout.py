from playwright.sync_api import Page, expect
import re


def test_signout(page: Page, loginFixture):
    home_page = loginFixture
    home_page.get_by_role("link", name=" Me ").click()
    home_page.get_by_role("link", name="Sign Out", exact=True).click()
    expect(page).to_have_url(re.compile("https://joblinc.me/"))
