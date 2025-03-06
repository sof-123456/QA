from .base_page import BasePage
from ..locators import USERNAME, PASSWORD, SUBMIT , ERROR_MESSAGE , LOG_OUT, URL_LOGIN
from selenium.webdriver.common.by import By



class LoginPage(BasePage):
     
    def login(self, username_value, password_value):
        self.send_keys(USERNAME, username_value)
        self.send_keys(PASSWORD, password_value)
        self.click(SUBMIT,  By.ID)
    
    
    def get_error_message(self):
        return  self.get_text(ERROR_MESSAGE)
    

  