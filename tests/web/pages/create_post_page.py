from playwright.sync_api import Page
from .base_page import BasePage


class CreatePostPage(BasePage):

    def __init__(
        self, page: Page, start_page: str = "https://joblinc.me/post/create"
    ):
        super().__init__(page, start_page)

        self.text_input = self.page.get_by_role(
            "textbox", name="Enter your text here:"
        )
        self.submit_button = self.page.get_by_role("button", name="Submit")
        self.cancel_button = self.page.get_by_role("button", name="Cancel")

        self.content_section = page.locator("div.min-w-0.mr-3.ml-3").nth(2)
        self.paragraph = self.content_section.locator("p")

    def create_post(self, text: str) -> None:
        self.text_input.click()
        self.text_input.fill(text)
        self.submit_button.click()

    def cancel_post(self) -> None:
        self.cancel_button.click()
