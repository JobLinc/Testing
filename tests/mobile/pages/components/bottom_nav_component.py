from appium.webdriver.common.appiumby import AppiumBy
from ..base_page import BasePage
from ..screens.my_network_page import MyNetworkPage


class BottomNavComponent(BasePage):
    """Component for handling the bottom navigation."""

    BOTTOM_NAV = (
        AppiumBy.XPATH,
        '//android.view.View[@content-desc="core_bottombar_container"]/android.view.View',
    )

    HOME_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Home\nTab 1 of 5")',
    )

    MY_NETWORK_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("My Network\nTab 2 of 5")',
    )
    POST_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Post\nTab 3 of 5")',
    )
    NOTIFICATION_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Notifications\nTab 4 of 5")',
    )
    JOBS_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Jobs\nTab 5 of 5")',
    )

    def verify_page_loaded(self, timeout: int = 10) -> None:
        """Ensures the bottom nav is loaded by checking for a key element."""
        self.wait_for_element(self.BOTTOM_NAV, timeout)

    def navigate_to_home(self):
        self.click(self.HOME_BUTTON)

    def navigate_to_my_network(self):
        self.click(self.MY_NETWORK_BUTTON)
        return MyNetworkPage(self.driver)

    def navigate_to_post(self):
        self.click(self.POST_BUTTON)

    def navigate_to_notifications(self):
        self.click(self.NOTIFICATION_BUTTON)

    def navigate_to_jobs(self):
        self.click(self.JOBS_BUTTON)
