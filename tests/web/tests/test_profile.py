from playwright.sync_api import Page, expect
from ..pages.profile_page import (
    update_cover_photo,
    get_user_id,
    update_profile_photo,
    add_experience,
    add_skill,
    delete_experience,
    edit_experience,
)
from ..config import IMAGE1_PATH, IMAGE2_PATH, EXPERIENCE, SKILL
import re


def test_add_experience(page: Page, profileFixture):
    profileFixture
    add_experience(page, EXPERIENCE)
    if page.locator("button.mt-2:has-text('Show all')").is_visible():
        page.locator("button.mt-2:has-text('Show all')").click()
        expect(
            page.locator(
                f'div.flex.flex-col:has-text("{EXPERIENCE["title"]}")'
            ).first
        ).to_be_visible()
    else:
        expect(
            page.locator(
                f'div.flex-col:has(span.font-medium:text("{EXPERIENCE["title"]}")):has-text("{EXPERIENCE["company"]}")'
            )
        ).to_be_visible()


"""def test_add_skills(page:Page , profileFixture):
    profileFixture
    add_skill(page , SKILL)"""


def test_edit_experience(page: Page, profileFixture):
    title = f'{EXPERIENCE["title"]} edited'
    company = f'{EXPERIENCE["company"]} edited'
    profileFixture
    edit_experience(page, EXPERIENCE)
    if page.locator("button.mt-2:has-text('Show all')").is_visible():
        page.locator("button.mt-2:has-text('Show all')").click()
        expect(
            page.locator(
                # f'div.flex.flex-col:has-text(/{re.escape(EXPERIENCE["title"])}.*edited/)'
            ).first
        ).to_be_visible()
    else:
        expect(
            page.locator(
                f'div.flex-col:has(span.font-medium:text("{title}")):has-text("{company}")'
            )
        ).to_be_visible()


def test_delete_experience(page: Page, profileFixture):

    title = f'{EXPERIENCE["title"]} edited'
    company = f'{EXPERIENCE["company"]} edited'

    profileFixture
    delete_experience(page)
    if page.locator("button.mt-2:has-text('Show all')").is_visible():
        page.locator("button.mt-2:has-text('Show all')").click()
        expect(
            page.locator(
                # f'div.flex.flex-col:has-text(/{re.escape(EXPERIENCE["title"])}.*edited/)'
            ).first
        ).not_to_be_visible()
    else:
        expect(
            page.locator(
                f'div.flex-col:has(span.font-medium:text("{title}")):has-text("{company}")'
            )
        ).not_to_be_visible()
