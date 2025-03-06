import pytest
from ..pages.Home import HomePage  
from ..pages.login import LoginPage
from ..pages.user_page import UserPage
from ..locators import ERROR_MESSAGE, URL_LOGIN
import allure
from  ..data import *

@allure.feature("Login Tests")
@pytest.mark.positive
def test_valid_login(driver):
    login_page = LoginPage(driver)  
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    assert login_page.get_current_url() == "https://practicetestautomation.com/logged-in-successfully/", "Invalid redirection"
    
    home_page = HomePage(driver)  
    assert home_page.get_success_message() ==SUCCESS_LOGIN_MESSAGE, "Login failed"

@allure.feature("Login Tests")
@pytest.mark.negative
@pytest.mark.parametrize("username_input, password_input, expected_message", [
     (INVALID_USERNAME, VALID_PASSWORD, ERROR_INVALID_USERNAME),  
     (VALID_USERNAME, INVALID_PASSWORD, ERROR_INVALID_PASSWORD),    
     (INVALID_USERNAME, INVALID_PASSWORD, ERROR_INVALID_USERNAME)  
 ])
def test_invalid_login(driver, username_input, password_input,expected_message):
      login_page=LoginPage(driver)
      login_page.login(username_input, password_input)
      login_page.scroll_until_element_visible(ERROR_MESSAGE)
     
      assert   login_page.get_error_message () == expected_message, f"Expected '{expected_message}', but got '{login_page.get_error_message()}'"     




@allure.feature("Logout Tests")
def test_logout(driver ):
     test_valid_login(driver)
     user_page=UserPage(driver)
     user_page.logout()
    
     assert  user_page.get_current_url()==URL_LOGIN


