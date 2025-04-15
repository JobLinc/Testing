from playwright.sync_api import Page
import re


def get_user_id(page: Page) -> str:
    user_id = page.url.split("/profile/")[-1]
    return user_id


def update_cover_photo(page: Page, image_path: str) -> None:
    page.get_by_role("button", name="camera_alt").click()
    page.locator('label[for="file-input"] span.material-icons').click()
    file_input = page.locator("input[type='file']")
    file_input.set_input_files(str(image_path))
    page.get_by_role("button", name="Confirm picture").click()
    # page.wait_for_timeout(10000)


def update_profile_photo(page: Page, image_path: str) -> None:
    page.get_by_role("img", name="Profile").click()
    page.locator("label").click()
    page.locator("body").set_input_files(str(image_path))
    page.get_by_role("button", name="Confirm Picture").click()


def add_experience(page: Page, EXPERIENCE) -> None:
    page.get_by_role("button", name="add").nth(1).click()
    page.locator("input[name='title']").fill(EXPERIENCE["title"])
    page.locator('input[name="company"]').fill(EXPERIENCE["company"])
    page.get_by_role("combobox").first.select_option(
        str(EXPERIENCE["start_month"])
    )
    page.get_by_role("combobox").nth(1).select_option(
        str(EXPERIENCE["start_year"])
    )
    page.get_by_role("combobox").nth(2).select_option(
        str(EXPERIENCE["end_month"])
    )
    page.get_by_role("combobox").nth(3).select_option(
        str(EXPERIENCE["end_year"])
    )
    page.locator('textarea[name="headline"]').fill(EXPERIENCE["description"])
    page.get_by_role("button", name="Add", exact=True).click()


def edit_experience(page: Page, EXPERIENCE) -> None:
    page.get_by_role("button", name="Edit").nth(1).click()
    page.get_by_role("button", name="Edit").nth(-1).click()

    page.locator("input[name='title']").fill(EXPERIENCE["title"] + " edited")
    page.locator('input[name="company"]').fill(
        EXPERIENCE["company"] + " edited"
    )

    page.get_by_role("combobox").first.select_option(
        str(EXPERIENCE["start_month"] + 1)
    )
    page.get_by_role("combobox").nth(1).select_option(
        str(EXPERIENCE["start_year"] + 1)
    )
    page.get_by_role("combobox").nth(2).select_option(
        str(EXPERIENCE["end_month"] + 1)
    )
    page.get_by_role("combobox").nth(3).select_option(
        str(EXPERIENCE["end_year"] + 1)
    )
    page.locator('textarea[name="headline"]').fill(
        EXPERIENCE["description"] + " edited"
    )
    page.get_by_role("button", name="Save", exact=True).click()


def delete_experience(page: Page) -> None:
    page.locator("button.mt-2:has-text('Show all')").click()
    page.get_by_role("button", name="Edit").nth(-1).click()

    page.get_by_role("button", name="Delete").nth(-1).click()
    page.get_by_role("button", name="Confirm").click()


def add_skill(page: Page, SKILL) -> None:
    page.get_by_role("button", name="Add skill").click()
    page.locator("form").get_by_role("textbox").fill(SKILL["name"])
    page.get_by_role("combobox").select_option(str(SKILL["level"]))
    page.get_by_role("button", name="Add", exact=True).click()
