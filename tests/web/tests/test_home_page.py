from playwright.sync_api import Page, expect
from ..config import (
    LOGIN_FNAME,
    LOGIN_LNAME,
    NEWPOST,
    COMMENT,
)
import re
from ..pages.home_page import comment

"""
def test_go_to_messages(page: Page, loginFixture):
    home_page = loginFixture
    home_page.get_by_role("link", name=" Messaging").click()
    expect(
        page.get_by_role("heading", name="Messaging"),
        "Messaging",
    ).to_be_visible()


def test_go_to_network(page: Page, loginFixture):
    home_page = loginFixture
    home_page.get_by_role("link", name="My Network").click()
    expect(page.get_by_text("Manage my network")).to_be_visible()


def test_go_to_profile(page: Page, loginFixture):
    home_page = loginFixture
    home_page.get_by_role("link", name=" Me ").click()
    expect(
        page.get_by_role("heading", name=f"{LOGIN_FNAME} {LOGIN_LNAME}")
    ).to_be_visible()


def test_new_post(page: Page, loginFixture) -> None:
    home_page = loginFixture
    # page.get_by_role("textbox", name="Write a new post...").click()
    home_page.get_by_role("textbox", name="Write a new post...").fill(
        f"{NEWPOST}"
    )
    home_page.get_by_role("button", name="send", exact=True).click()
    expect(page.get_by_text(f"{NEWPOST}").first).to_be_visible()

def test_create_delete_post(page: Page, loginFixture) -> None:
    home_page = loginFixture
    home_page.get_by_role("textbox", name="Write a new post...").fill(f"{NEWPOST}")
    home_page.get_by_role("button", name="send", exact=True).click()
    with page.expect_response(
        lambda response: response.url.endswith("/api/post/add") and response.status == 200
    ):
        expect(home_page.get_by_text(f"{NEWPOST}").first).to_be_visible(timeout=10000)
    
    page.get_by_text("more_horiz").first.click()
    page.get_by_role("button", name="Delete").click()
    page.get_by_role("button", name="Confirm").click()
    
    page.goto("https://joblinc.me/home")
    expect(home_page.get_by_text(f"{NEWPOST}").first).not_to_be_visible(timeout=10000)
    
    
    
def test_react_unreact_post(page: Page, loginFixture) -> None:
    home_page = loginFixture
    home_page.get_by_role(
            "button", name="React"
        ).first.hover()
    home_page.locator("div").filter(has_text=re.compile(r"^Celebrate$")).first.click()
    
    expect(home_page.locator("div").filter(has_text="Added!").nth(3)).to_be_visible()
    expect(home_page.get_by_role("button", name="Celebrate")).to_be_visible()
    
    home_page.locator("div").filter(has_text=re.compile(r"^Remove$")).click()
    #home_page.locator("div").first.filter(has_text=re.compile(r"^LikeRemoveCelebrateSupportFunnyLoveInsightful$")).get_by_role("button").click()
   
    expect(home_page.locator("div").filter(has_text="Removed!").nth(3)).to_be_visible()
    """


def test_comment_post(page: Page, loginFixture) -> None:
    home_page = loginFixture
    comment(home_page)
    expect(
        home_page.get_by_role("paragraph").filter(has_text=f"{COMMENT}").nth(-1)
    ).to_be_visible()

    # page.locator('div.flex.flex-wrap.w-1\\/1.rounded-xl.relative.py-2:has(p.font-bold:text("last three"))').locator('button:text("more_horiz")')
    # home_page.get_by_role("button", name="Edit").click()

    # page.locator("[id=\"headlessui-menu-button-\\:r2b\\:\"]").click()
    # page.get_by_role("button", name="Edit").click()

    # page.get_by_role("textbox", name="Speak your mind...").fill(f"{COMMENT} EDITED")
    # page.get_by_role("button", name="Edit").click()
    # page.goto("https://joblinc.me/home")
    # expect(page.get_by_role("main")).to_contain_text(f"{COMMENT} EDITED")

    # page.locator("[id=\"headlessui-menu-button-\\:r1p\\:\"]").click()
    # page.get_by_test_id("Delete 6816d1aacaf68280e5423b46").click()
    # page.get_by_role("button", name="Confirm").click()
    # expect(page.get_by_role("main")).not_to_contain_text(f"{COMMENT} EDITED")
