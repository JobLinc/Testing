from playwright.sync_api import Page, expect
from ..pages.post_page import PostPage
from ..config import COMMENT, REPLY


def test_valid_like(page: Page) -> None:

    post_page = PostPage(page)
    post_page.like_post()
    expect(post_page.like_button.nth(0)).to_have_text("Liked")


def test_valid_comment(page: Page) -> None:
    post_page = PostPage(page)
    post_page.comment_post(COMMENT)
    expect(post_page.check_comment_text(COMMENT)).to_be_visible()


def test_valid_like_comment(page: Page) -> None:
    post_page = PostPage(page)
    post_page.like_comment()
    expect(post_page.like_button.nth(1)).to_have_text("Liked")


def test_valid_reply_comment(page: Page) -> None:
    post_page = PostPage(page)
    post_page.reply_comment(REPLY)
    expect(post_page.check_comment_text(REPLY)).to_be_visible()


def test_valid_like_reply(page: Page) -> None:
    post_page = PostPage(page)
    post_page.like_reply()
    expect(post_page.like_reply_comment).to_have_text("Liked")


def test_valid_follow_user(page: Page) -> None:
    post_page = PostPage(page)
    post_page.follow_user()
    expect(post_page.follow_button).to_have_text("Followed")


def test_valid_edit_post(page: Page) -> None:
    post_page = PostPage(page)
    post_page.edit_post(COMMENT)
    expect(post_page.paragraph).to_have_text(COMMENT)


def test_valid_delete_post(page: Page) -> None:
    post_page = PostPage(page)
    post_page.delete_post()
    expect(page).to_have_url("https://joblinc.me/")


def test_valid_hide_unhide_post(page: Page) -> None:
    post_page = PostPage(page)
    post_page.hide_post()
    expect(post_page.undo_button).to_be_visible()
    expect(post_page.post_section).to_have_count(1)
    post_page.unhide_post()
    expect(post_page.undo_button).to_be_hidden()
    expect(post_page.post_section).to_have_count(2)
