from playwright.sync_api import Page, expect
import re


def signin_with_email(page: Page, email: str) -> None:
    page.goto("https://joblinc.me/Signin")
    page.fill("input[name='email']", email)
    page.fill("input[name='password']", "last123")
    signin_button = page.get_by_role("button", name="Sign in")
    signin_button.click()


def confirm_email(page: Page) -> None:
    page.get_by_role("link", name=" Me ").click()
    page.get_by_role("link", name="Settings & Privacy", exact=True).click()
    page.get_by_text("Sign in & security").click()
    page.locator("div").filter(
        has_text=re.compile(r"^Email addresses$")
    ).click()
    page.get_by_role("button", name="Confirm email").click()
    page.locator(".w-10").first.fill("5")
    page.locator(".flex > .flex > input:nth-child(2)").fill("4")
    page.locator("input:nth-child(3)").fill("3")
    page.locator("input:nth-child(4)").fill("2")
    page.locator("input:nth-child(5)").fill("1")
    page.locator("input:nth-child(6)").fill("8")
    expect(
        page.get_by_role("heading", name="Wrong OTP entered")
    ).to_be_visible()
    page.get_by_test_id("close-button").click()


def change_email(page: Page, new_email: str):
    page.get_by_role("button", name="Update email").click()
    page.get_by_role("textbox", name="Email *").click()
    page.get_by_role("textbox", name="Email *").fill(new_email)
    page.get_by_role("button", name="Update Email").click()
    expect(
        page.get_by_role("heading", name="Email updated successfully!")
    ).to_be_visible()
    page.get_by_role("button", name="Continue").click()
