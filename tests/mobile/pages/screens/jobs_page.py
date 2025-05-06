from ..base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from ..components.post_job import PostJobPage


class JobsPage(BasePage):
    """Jobs page containing components"""

    SEARCH_JOBS = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText")',
    )

    MY_JOBS_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("My Jobs")',
    )

    POST_JOB_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Post a free job")',
    )

    JOB_CARDS = (
        AppiumBy.XPATH,
        "//*[starts-with(@content-desc, 'job_card')]",
    )

    CARD_ITEM = (AppiumBy.XPATH, "//android.view.View/android.view.View")

    def __init__(self, driver):
        super().__init__(driver)

    def verify_page_loaded(self, timeout: int = 5) -> None:
        """Ensure the network page is loaded."""
        self.wait_for_element(self.MY_JOBS_BUTTON)
        self.wait_for_element(self.POST_JOB_BUTTON)

    def go_to_create_job(self) -> PostJobPage:
        self.click(self.POST_JOB_BUTTON)
        return PostJobPage(self.driver)

    def get_all_jobs(self):

        self.wait_for_element(self.JOB_CARDS)
        job_cards = self.driver.find_elements(*self.JOB_CARDS)

        for job_card in job_cards:
            element = job_card.find_element(*self.CARD_ITEM)
            job_title, full_name, username, location, experience, salary = (
                element.get_attribute("content-desc").split("\n")
            )
            print(
                f"{job_title} - {full_name} - {username} - {location} - {experience} - {salary}"
            )
