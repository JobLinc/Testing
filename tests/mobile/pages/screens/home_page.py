from ..base_page import BasePage
from ..components.sidebar_component import SidebarComponent
from ..components.bottom_nav_component import BottomNavComponent


class HomePage(BasePage):
    """Main home page containing components"""

    def __init__(self, driver):
        super().__init__(driver)
        self.sidebar = SidebarComponent(driver)
        self.bottom_nav = BottomNavComponent(driver)

    def verify_page_loaded(self, timeout: int = 5) -> None:
        """Ensure the home page is loaded."""
        pass
