from playwright.sync_api import Page, expect
import re


def search_for_user_send_request(page: Page):
    page.get_by_role("textbox", name="Search").fill("last seven")
    page.get_by_role("button", name="Show All Results").click()
    page.locator("div").filter(
        has_text=re.compile(r"^last threeFollow$")
    ).get_by_test_id("follow-button").click()

    page.locator("div").filter(
        has_text=re.compile(
            r"^last threeUnfollowCairo, Egypt0 mutual connectionsLinc$"
        )
    ).get_by_test_id("linc-button").click()


def accept_request(page: Page):
    page.get_by_role("link", name=" My Network").click()
    page.get_by_test_id("accept-inv-button").click()
