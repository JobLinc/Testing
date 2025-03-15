import pytest
from pytest import FixtureRequest
from typing import Generator
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext
from .config import HEADLESS, BROWSERS


@pytest.fixture(params=BROWSERS)
def page(request: FixtureRequest) -> Generator[Page, None, None]:
    """Fixture to provide a Playwright page object for each browser."""
    with sync_playwright() as p:
        browser: Browser = getattr(p, request.param).launch(headless=HEADLESS)
        context: BrowserContext = browser.new_context()
        page: Page = context.new_page()

        yield page

        page.close()
        browser.close()
