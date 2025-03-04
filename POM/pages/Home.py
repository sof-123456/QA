from .base_page import BasePage
from ..locators import  SUCCESS_MESSAGE

class HomePage(BasePage):
   
    def get_success_message(self):
        return self.get_text(SUCCESS_MESSAGE)
