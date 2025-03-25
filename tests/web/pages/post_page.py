from playwright.sync_api import Page
from .base_page import BasePage
import re


class PostPage(BasePage):

    def __init__(self, page: Page, start_page: str = "https://joblinc.me/post"):
        super().__init__(page, start_page)

        # all likes buttons
        self.like_button = page.locator(
            "button:has(p.material-icons:text('thumb_up')) >> text=Like"
        )

        self.comment_button = page.get_by_role(
            "button", name="insert_comment Comment"
        ).first
        self.comment_input = page.get_by_role("textbox", name="Write a comment")
        # all comments send
        self.comment_send_button = page.get_by_role(
            "button", name="send", exact=True
        )

        self.reply_comment_button = page.get_by_role(
            "button", name="Reply"
        ).first
        self.reply_comment_input = page.get_by_role(
            "textbox", name="Write a reply"
        )
        self.like_reply_comment = like_button = page.locator(
            "button:has-text('Like'), button:has-text('Liked')"
        ).nth(1)

        self.follow_button = page.get_by_text("Follow").first
        # self.follow_button = page.locator("p.text-red-600.font-medium:text-is('Follow')")

        self.post_section = page.locator(
            "div.flex.flex-wrap.w-1\\/1.bg-lightGray.rounded-xl.relative"
        )
        self.content_section = page.locator("div.min-w-0.mr-3.ml-3").nth(0)
        self.paragraph = self.content_section.locator("p").nth(0)

        self.options_button = page.get_by_test_id("Options 0")

        self.edit_option = page.get_by_role("button", name="Edit").first
        self.post_text = page.get_by_text("Lorem ipsum dolor sit amet,").nth(0)
        self.submit_edit = page.get_by_role("button", name="Submit")

        self.delete_option = page.get_by_test_id("Delete 0")

        self.hide_button = page.get_by_role("button", name="clear").first
        self.undo_button = page.get_by_role("button", name="undo")

    def like_post(self) -> None:
        self.like_button.nth(0).click()

    def check_comment_text(self, comment: str) -> str:
        return self.page.locator(f"p.text-sm:text-is('{comment}')")

    def comment_post(self, comment: str) -> None:
        self.comment_button.click()
        self.comment_input.fill(comment)
        self.comment_send_button.nth(0).click()

    def like_comment(self) -> None:
        self.comment_button.click()
        self.like_button.nth(1).click()

    def reply_comment(self, reply: str) -> None:
        self.comment_button.click()
        self.reply_comment_button.click()
        self.reply_comment_input.fill(reply)
        self.comment_send_button.nth(1).click()

    def like_reply(self) -> None:
        self.comment_button.click()
        self.reply_comment_button.click()
        self.like_reply_comment.click()

    def follow_user(self) -> None:
        self.follow_button.click()

    def edit_post(self, edit_text: str) -> None:
        self.options_button.click()
        self.edit_option.click()
        self.post_text.click()
        self.post_text.fill(edit_text)
        self.submit_edit.click()

    def delete_post(self) -> None:
        self.options_button.click()
        self.delete_option.click()

    def hide_post(self) -> None:
        self.hide_button.click()

    def unhide_post(self) -> None:
        self.undo_button.click()
