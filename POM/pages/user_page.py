from .base_page import BasePage
from ..locators import LOG_OUT

class UserPage(BasePage):
    def logout(self):
        element=self.wait_for_elements(LOG_OUT)
        element.click()
        