from playwright.sync_api import Page
import re


def get_user_id(page: Page) -> str:
    user_id = page.url.split("/profile/")[-1]
    return user_id


def update_cover_photo(page: Page, image_path) -> None:
    page.get_by_role("button", name="camera_alt").click()
    page.locator('label[for="file-input"] span.material-icons').click()
    file_input = page.locator("input[type='file']")
    file_input.set_input_files(str(image_path))
    page.get_by_role("button", name="Confirm picture").click()
    page.wait_for_timeout(5000)

    # page.locator("span").filter(has_text="edit").click()
    # page.locator("body").set_input_files("Screenshot 2025-03-10 210503.png")
    # page.get_by_role("button", name="Confirm Picture").click()


def update_profile_photo(page: Page, image_path) -> None:

    page.get_by_role("img", name="Profile").click()
    page.locator("span").filter(has_text="edit").click()
    # page.locator('label[for="file-input"] span.material-icons').click()
    file_input = page.locator("input[type='file']")
    file_input.set_input_files(str(image_path))
    page.get_by_role("button", name="Confirm Picture").click()
    page.wait_for_timeout(5000)


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
    page.locator("div").filter(
        has_text=re.compile(rf"^{re.escape(EXPERIENCE['title'])}.*edit$")
    ).get_by_role("button").click()

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


def delete_experience(page: Page, EXPERIENCE) -> None:
    page.get_by_role("button", name="Edit").nth(1).click()
    page.locator("div").filter(
        has_text=re.compile(rf"^{re.escape(EXPERIENCE['title'])}.*edit$")
    ).get_by_role("button").click()

    page.get_by_role("button", name="Delete").click()
    page.get_by_role("button", name="Confirm").click()


def add_certificate(page: Page, CERTIFICATE) -> None:
    page.get_by_role("button", name="add").nth(2).click()

    page.locator("div").filter(has_text=re.compile(r"^Name$")).get_by_role(
        "textbox"
    ).click()
    page.locator("div").filter(has_text=re.compile(r"^Name$")).get_by_role(
        "textbox"
    ).fill(CERTIFICATE["name"])
    page.locator("div").filter(
        has_text=re.compile(r"^Organization$")
    ).get_by_role("textbox").click()
    page.locator("div").filter(
        has_text=re.compile(r"^Organization$")
    ).get_by_role("textbox").fill(CERTIFICATE["organization"])
    page.get_by_role("combobox").first.select_option(
        str(CERTIFICATE["start_month"])
    )
    page.get_by_role("combobox").nth(1).select_option(
        str(CERTIFICATE["start_year"])
    )
    page.get_by_role("combobox").nth(2).select_option(
        str(CERTIFICATE["end_month"])
    )
    page.get_by_role("combobox").nth(3).select_option(
        str(CERTIFICATE["end_year"])
    )
    page.get_by_role("button", name="Add", exact=True).click()


def edit_certificate(page: Page, CERTIFICATE) -> None:
    page.get_by_role("button", name="edit").nth(2).click()
    page.locator("div").filter(
        has_text=re.compile(rf"^{re.escape(CERTIFICATE['name'])}.*edit$")
    ).get_by_role("button").click()
    page.locator("div").filter(has_text=re.compile(r"^Name$")).get_by_role(
        "textbox"
    ).click()
    page.locator("div").filter(has_text=re.compile(r"^Name$")).get_by_role(
        "textbox"
    ).fill(CERTIFICATE["name"] + " edited")
    page.locator("div").filter(
        has_text=re.compile(r"^Organization$")
    ).get_by_role("textbox").click()
    page.locator("div").filter(
        has_text=re.compile(r"^Organization$")
    ).get_by_role("textbox").fill(CERTIFICATE["organization"] + " edited")
    page.get_by_role("combobox").first.select_option(
        str(CERTIFICATE["start_month"] + 1)
    )
    page.get_by_role("combobox").nth(1).select_option(
        str(CERTIFICATE["start_year"] + 1)
    )
    page.get_by_role("combobox").nth(2).select_option(
        str(CERTIFICATE["end_month"] + 1)
    )
    page.get_by_role("combobox").nth(3).select_option(
        str(CERTIFICATE["end_year"] + 1)
    )
    page.get_by_role("button", name="Save", exact=True).click()


def delete_certificate(page: Page, CERTIFICATE) -> None:
    page.get_by_role("button", name="Edit").nth(2).click()
    page.locator("div").filter(
        has_text=re.compile(rf"^{re.escape(CERTIFICATE['name'])}.*edit$")
    ).get_by_role("button").click()

    page.get_by_role("button", name="Delete").click()
    page.get_by_role("button", name="Confirm").click()


def add_skill(page: Page, SKILL) -> None:
    page.get_by_role("button", name="add").nth(3).click()

    page.locator("form").get_by_role("textbox").fill(SKILL["name"])
    page.get_by_role("combobox").select_option(str(SKILL["level"]))
    page.get_by_role("button", name="Add", exact=True).click()


def edit_skill(page: Page, SKILL) -> None:
    page.get_by_role("button", name="Edit").nth(3).click()
    page.locator("div").filter(
        has_text=re.compile(rf"^{re.escape(SKILL['name'])}.*edit$")
    ).get_by_role("button").click()
    page.locator("form").get_by_role("textbox").fill(SKILL["name"] + " edited")
    page.get_by_role("combobox").select_option(str(SKILL["level"] + 1))
    page.get_by_role("button", name="Save", exact=True).click()


def delete_skill(page: Page, SKILL) -> None:
    page.get_by_role("button", name="Edit").nth(3).click()
    page.locator("div").filter(
        has_text=re.compile(rf"^{re.escape(SKILL['name'])}.*edit$")
    ).get_by_role("button").click()

    page.get_by_role("button", name="Delete").click()
    page.get_by_role("button", name="Confirm").click()


def edit_user_data(page: Page, USER_DATA) -> None:

    page.get_by_role("button", name="Edit").nth(0).click()
    page.locator("input[name='firstname']").fill(USER_DATA["first_name"])
    page.locator("input[name='lastname']").fill(USER_DATA["last_name"])
    page.locator("textarea[name='headline']").fill(USER_DATA["headline"])
    page.locator("input[name='city']").fill(USER_DATA["city"])
    page.get_by_role("button", name="Save Changes", exact=True).click()
