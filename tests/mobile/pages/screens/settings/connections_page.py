from appium.webdriver.common.appiumby import AppiumBy
from ...base_page import BasePage


class ConnectionsPage(BasePage):
    """Page object for the connections screen."""

    CONNECTION_LIST = (
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View',
    )

    CONNECTION_ITEM = (
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/*',
    )

    REMOVE_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(1)',
    )

    CONFIRM_REMOVE_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Remove connection")',
    )

    def verify_page_loaded(self, timeout: int = 5) -> None:
        """Ensure the connections page is loaded."""
        self.wait_for_element(self.CONNECTION_LIST, timeout)

    def get_connections(self) -> list[dict]:
        """Retrieves the list of connections displayed on the screen."""
        connection_elements = self.driver.find_elements(*self.CONNECTION_ITEM)
        connections = []

        for element in connection_elements:
            connection_name = (
                element.get_attribute("content-desc") or element.text
            )
            connections.append({"name": connection_name, "element": element})

        return connections

    def remove_connection(self, connection_name: str) -> None:
        """Find and remove a specific connection by name."""
        connections = self.get_connections()

        for connection in connections:
            if connection["name"] == connection_name:
                connection_element = connection["element"]

                remove_button = connection_element.find_element(
                    *self.REMOVE_BUTTON
                )
                remove_button.click()

                self.wait_for_element(self.CONFIRM_REMOVE_BUTTON).click()

                return

        raise ValueError(f"Connection '{connection_name}' not found")
