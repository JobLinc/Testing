from playwright.sync_api import Page, expect
from ..pages.create_post_page import CreatePostPage

from ..config import NEWPOST


def test_valid_create_post(page: Page) -> None:
    create_post_page = CreatePostPage(page)
    create_post_page.create_post(NEWPOST)
    expect(page).to_have_url("https://joblinc.me/post")
    expect(create_post_page.paragraph).to_have_text(NEWPOST)


def test_valid_cancel_post(page: Page) -> None:
    create_post_page = CreatePostPage(page)
    create_post_page.cancel_post()
    expect(page).to_have_url("https://joblinc.me/")
