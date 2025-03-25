from appium.webdriver.common.appiumby import AppiumBy
from ..base_page import BasePage
from ..screens.settings.settings_page import SettingsPage
from ..screens.settings.connections_page import ConnectionsPage


class SidebarComponent(BasePage):
    """Component for handling the sidebar navigation."""

    PROFILE_BUTTON = (
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]',
    )
    VIEW_CONNECTIONS = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("View my connections")',
    )
    VIEW_ANALYTICS = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("View all analytics")',
    )
    PUZZLE_GAMES = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Puzzle games")',
    )
    SAVED_POSTS = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Saved posts")',
    )
    GROUPS = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Groups")',
    )
    SETTINGS = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Settings")',
    )

    def verify_page_loaded(self, timeout: int = 10) -> None:
        """Ensures the sidebar is loaded by checking for a key element."""
        self.wait_for_element(self.PROFILE_BUTTON, timeout)

    def navigate_to_settings(self) -> SettingsPage:
        """Navigates to the Settings page."""
        self.click(self.PROFILE_BUTTON)
        self.click(self.SETTINGS)
        return SettingsPage(self.driver)

    def navigate_to_connections(self) -> ConnectionsPage:
        """Navigates to the Connections page."""
        self.click(self.PROFILE_BUTTON)
        self.click(self.VIEW_CONNECTIONS)
        return ConnectionsPage(self.driver)
