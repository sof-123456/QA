import pytest
from ..pages.Home import HomePage  
from ..pages.login import LoginPage
from ..pages.user_page import UserPage
from ..locators import ERROR_MESSAGE, URL_LOGIN
import allure


@allure.feature("Login Tests")
@pytest.mark.positive
def test_valid_login(driver):
    login_page = LoginPage(driver)  
    login_page.login("student", "Password123")
    assert login_page.get_current_url() == "https://practicetestautomation.com/logged-in-successfully/", "Invalid redirection"
    home_page = HomePage(driver)  
    assert home_page.get_success_message() == "Logged In Successfullykdkdkdk", "Login failed"

@allure.feature("Login Tests")
@pytest.mark.negative
@pytest.mark.parametrize("username_input, password_input, expected_message", [
     ("incorrectUser", "Password123", "Your username is invalid"),  
     ("student", "123", "Your password is invalid!"),    
     ("incorrectUser", "123", "Your username is invalid!")  
 ])
def test_invalid_login(driver, username_input, password_input,expected_message):
      login_page=LoginPage(driver)
      login_page.login(username_input, password_input)
     
      assert   login_page.get_error_message () == expected_message, f"Expected '{expected_message}', but got '{login_page.get_error_message()}'"     


@allure.feature("Logout Tests")
def test_logout(driver ):
     test_valid_login(driver)
     user_page=UserPage(driver)
     user_page.logout()
    
     assert  user_page.get_current_url()==URL_LOGIN


