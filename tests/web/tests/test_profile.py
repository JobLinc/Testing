from playwright.sync_api import Page, expect
from ..pages.profile_page import (
    update_cover_photo,
    get_user_id,
    update_profile_photo,
    add_experience,
    add_skill,
    edit_skill,
    delete_skill,
    delete_experience,
    edit_experience,
    add_certificate,
    edit_certificate,
    delete_certificate,
    edit_user_data,
)
from ..config import (
    IMAGE1_PATH,
    IMAGE2_PATH,
    EXPERIENCE,
    SKILL,
    CERTIFICATE,
    NEW_USER,
)
import re


def test_add_experience(page: Page, profileFixture):
    profileFixture
    add_experience(page, EXPERIENCE)

    # more than 4 experiences
    if page.get_by_role(
        "button", name=re.compile(r"Show all \d+ experiences")
    ).is_visible():
        page.get_by_role(
            "button", name=re.compile(r"Show all \d+ experiences")
        ).click()
        page.locator(
            f'div.flex.flex-col:has-text("{EXPERIENCE["title"]}")'
        ).first.highlight()

        expect(
            page.locator(
                f'div.flex.flex-col:has-text("{EXPERIENCE["title"]}")'
            ).first
        ).to_be_visible()

    else:
        # less than 3 experiences
        page.locator(
            f'div.flex-col:has(span.font-medium:text("{EXPERIENCE["title"]}"))'
        ).highlight()
        expect(
            page.locator(
                f'div.flex-col:has(span.font-medium:text("{EXPERIENCE["title"]}"))'
            )
        ).to_be_visible()

    # it doesnt handle 3 experiences for some reason because page.get_by_role("button", name="Show all 3 experiences").is_visible() is not working


def test_edit_experience(page: Page, profileFixture):
    title = f'{EXPERIENCE["title"]} edited'
    company = f'{EXPERIENCE["company"]} edited'
    profileFixture
    edit_experience(page, EXPERIENCE)
    if page.locator("button.mt-2:has-text('Show all')").is_visible():
        page.locator("button.mt-2:has-text('Show all')").click()
        expect(
            page.locator(
                f'div.flex.flex-col:has-text(/{re.escape(str(EXPERIENCE["title"]))}.*edited/)'
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
    delete_experience(page, EXPERIENCE)

    expect(
        page.locator(f'div.flex.flex-col:has-text("{title}")').first
    ).not_to_be_visible()


def test_valid_cover_photo(page: Page, profileFixture) -> None:
    profileFixture
    update_cover_photo(page, IMAGE1_PATH)
    # Check src matches Cloudinary pattern with your user ID
    userid = get_user_id(page)

    expect(page.locator('img[alt="Cover"]')).to_have_attribute(
        "src",
        re.compile(
            rf"https://res\.cloudinary\.com/dufshbyse/image/upload/.*{userid}.*\.png"
        ),
    )


def test_valid_profile_photo(page: Page, profileFixture) -> None:
    profileFixture
    update_profile_photo(page, IMAGE1_PATH)
    # Check src matches Cloudinary pattern with your user ID
    userid = get_user_id(page)

    expect(
        page.locator('img.w-32.h-32.rounded-full[alt="Profile"]')
    ).to_have_attribute(
        "src",
        re.compile(
            rf"https://res\.cloudinary\.com/dufshbyse/image/upload/.*profile/{userid}-\d+\.png",
            re.IGNORECASE,
        ),
    )


def test_add_certificate(page: Page, profileFixture) -> None:
    profileFixture
    add_certificate(page, CERTIFICATE)
    page.get_by_role("button", name="edit").nth(2).click()
    page.locator(
        f'div.flex.flex-col:has-text("{CERTIFICATE["name"]}")'
    ).first.highlight()

    expect(
        page.locator(
            f'div.flex.flex-col:has-text("{CERTIFICATE["name"]}")'
        ).first
    ).to_be_visible()


def test_edit_certificate(page: Page, profileFixture) -> None:
    name = f'{CERTIFICATE["name"]} edited'
    organization = f'{CERTIFICATE["organization"]} edited'
    profileFixture
    edit_certificate(page, CERTIFICATE)
    page.get_by_role("button", name="edit").nth(2).click()

    expect(
        page.locator(
            f'div.flex-col:has(span.font-medium:text("{name}")):has-text("{organization}")'
        )
    ).to_be_visible()


def test_delete_certificate(page: Page, profileFixture):

    name = f'{CERTIFICATE["name"]} edited'
    profileFixture
    delete_certificate(page, CERTIFICATE)

    expect(
        page.locator(f'div.flex.flex-col:has-text("{name}")').first
    ).not_to_be_visible()


def test_add_skills(page: Page, profileFixture):
    profileFixture
    add_skill(page, SKILL)
    page.get_by_role("button", name="edit").nth(3).click()
    page.locator(
        f'div.flex.flex-col:has-text("{SKILL["name"]}")'
    ).first.highlight()

    expect(
        page.locator(f'div.flex.flex-col:has-text("{SKILL["name"]}")').first
    ).to_be_visible()


def test_edit_skill(page: Page, profileFixture):
    name = f'{SKILL["name"]} edited'
    profileFixture
    edit_skill(page, SKILL)

    expect(
        page.locator(f'div.flex-col:has(span.font-medium:text("{name}"))')
    ).to_be_visible()


def test_delete_skill(page: Page, profileFixture):

    name = f'{SKILL["name"]} edited'
    profileFixture
    delete_skill(page, SKILL)

    expect(
        page.locator(f'div.flex.flex-col:has-text("{name}")').first
    ).not_to_be_visible()


def test_edit_user_data(page: Page, profileFixture):
    profileFixture
    edit_user_data(page, NEW_USER)

    expect(page.locator("h1.text-2xl.font-bold.text-warmWhite")).to_have_text(
        f"{NEW_USER['first_name']} {NEW_USER['last_name']}"
    )
