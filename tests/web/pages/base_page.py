from playwright.sync_api import Page
from ..config import BASE_URL


class BasePage:
    def __init__(self, page: Page, start_url: str = BASE_URL):
        self.page = page
        self.start_page = start_url
        self.navigate(start_url)

    def navigate(self, url: str) -> None:
        self.page.goto(url)
