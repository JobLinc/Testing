from playwright.sync_api import Page, expect
from ..pages.connection_page import search_for_user_send_request, accept_request
from ..config import IMAGE1_PATH
import re


# chrome sends a request from test new
def test_connection(page: Page, loginFixture):
    browser = page.context.browser
    browser_type = browser.browser_type.name

    if browser_type == "chromium":
        loginFixture
        search_for_user_send_request(page)
        expect(page.get_by_test_id("unfollow-button")).to_be_visible()
        expect(page.get_by_test_id("pending-button")).to_be_visible()

    if browser_type == "webkit":
        page.goto("https://joblinc.me/Signin")
        page.fill("input[name='email']", "last3@email.com")
        page.fill("input[name='password']", "last123")
        signin_button = page.get_by_role("button", name="Sign in")
        signin_button.click()

        accept_request(page)
        expect(page.get_by_role("heading", name="test new")).to_be_visible()
        expect(
            page.get_by_text("test new is now a connection!×")
        ).to_be_visible()

        page.get_by_role("link", name=" Me ").click()
        page.get_by_role("button", name="View Profile").click()
        page.get_by_text("Connections:").click()
        expect(page.get_by_role("heading", name="test new")).to_be_visible()
        page.get_by_test_id("message-button").click()

        # chat with image

        page.get_by_role("textbox", name="Write a message...").fill(
            "first message"
        )
        # page.get_by_test_id("test-floatingWindow").get_by_role("button").nth(2).click()
        # page.get_by_test_id("test-floatingWindow").get_by_role("button").nth(2).set_input_files(IMAGE1_PATH)
        file_input = page.locator('[data-testid="input-file"]')
        file_input.set_input_files(IMAGE1_PATH)
        page.get_by_role("button", name="➤").click()
        expect(
            page.get_by_test_id("test-floatingWindow").get_by_text(
                "first message"
            )
        ).to_be_visible()
        page.get_by_test_id("close-button").click()

    # messages place
    # page.get_by_role("link", name=" Messaging").click()
    # page.wait_for_timeout(100000)
    # expect(page.get_by_text("You: first message").nth(1)).to_be_visible()
    # page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(4).click()
    # page.get_by_text("test new1 minute agoYou: first messageDeleteMark as Unread").click()


def test_remove_connection(page: Page, loginFixture):
    browser = page.context.browser
    browser_type = browser.browser_type.name

    if browser_type == "chromium":
        loginFixture
        page.get_by_role("textbox", name="Search").fill("last seven")
        page.get_by_role("button", name="Show All Results").click()
        page.get_by_role("heading", name="last three").click()
        page.get_by_role("button", name="More", exact=True).click()
        page.get_by_role("button", name="Unfollow").click()
        expect(
            page.locator("div").filter(has_text="Unfollowed").nth(3)
        ).to_be_visible()
        page.get_by_role("button", name="Remove Connection").click()
        expect(
            page.locator("div")
            .filter(has_text="User removed successfully!")
            .nth(3)
        ).to_be_visible()
        page.get_by_text("Connections:").click()
        expect(page.get_by_text("No connections found.")).to_be_visible()
