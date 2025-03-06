from .base_page import BasePage
from ..locators import LOG_OUT

class UserPage(BasePage):
    def logout(self):
        element=self.find_element__(LOG_OUT)
        element.click()
        