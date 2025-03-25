from ..base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class MyNetworkPage(BasePage):
    """My network page containing components"""

    MY_NETWORK_HEADING = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().description("Invitations")',
    )

    INVITATION_LIST = (
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View',
    )

    INVITATION_ITEM = (
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/*',
    )

    REMOVE_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(0)',
    )

    ACCEPT_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").instance(1)',
    )

    def __init__(self, driver):
        super().__init__(driver)

    def verify_page_loaded(self, timeout: int = 5) -> None:
        """Ensure the network page is loaded."""
        self.wait_for_element(self.MY_NETWORK_HEADING)

    def get_invitations(self) -> list[dict]:
        invitation_elements = self.driver.find_elements(*self.INVITATION_ITEM)
        invitations = []

        for element in invitation_elements:
            invitation_name = (
                element.get_attribute("content-desc") or element.text
            )
            invitations.append({"name": invitation_name, "element": element})

        return invitations

    def remove_invitation(self, invitation_name: str) -> None:
        """Find and remove a specific invitation by name."""
        invitations = self.get_invitations()

        for invitation in invitations:
            if invitation["name"] == invitation_name:
                invitation_element = invitation["element"]

                remove_button = invitation_element.find_element(
                    *self.REMOVE_BUTTON
                )
                remove_button.click()
                return

        raise ValueError(f"Invitation '{invitation_name}' not found")

    def accept_invitation(self, invitation_name: str) -> None:
        """Find and accept a specific invitation by name."""
        invitations = self.get_invitations()

        for invitation in invitations:
            if invitation["name"] == invitation_name:
                invitation_element = invitation["element"]

                accept_button = invitation_element.find_element(
                    *self.ACCEPT_BUTTON
                )
                accept_button.click()
                return

        raise ValueError(f"Invitation '{invitation_name}' not found")
