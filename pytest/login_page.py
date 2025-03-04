import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_UI(driver):
    
    logo = driver.find_element(By.XPATH, '//*[@id="site-title"]/a/img')
    menu_bar=driver.find_element(By.XPATH,'//*[@id="menu-primary-items"]')
    menu_links =menu_bar.find_elements(By.XPATH, './/a')


    expected_links = [
        "HOME",
        "AAAAA",
        "COURSES",
        "BLOG",
        "CONTACT",
    

    ]
    assert len(menu_links)==len(expected_links),"Number of menu items does not match expected"
    for i in range(len(menu_links)) :
        assert  menu_links[i].text == expected_links[i] , f"Menu item '{menu_links[i].text}' at index {i} is incorrect. Expected '{expected_links[i]}'"
  
    text_header = driver.find_element(By.XPATH, "//h2[contains(text(),'Test login')]")  
    username = driver.find_element(By.XPATH, '//*[@id="username"]')
    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    submit_button=driver.find_element(By.XPATH, '//*[@id="submit"]') 
    footer=driver.find_element(By.XPATH, '//*[@id="site-footer"]')
    
    
    text_block=driver.find_element(By.XPATH, '//*[@id="login"]/ul')
    full_text = text_block.text  
    expected_text = (
        "This is a simple Login page. Students can use this page to practice writing simple positive and negative LogIn tests. "
        "Login functionality is something that most of the test automation engineers need to automate.\n"
        "Use next credentials to execute Login:\n"
        "Username: student\n"
        "Password: Password123"
    
    )
     
    assert logo.is_displayed(), "Logo is not displayed"
    assert username.is_displayed(), "Username field is not displayed"
    assert password.is_displayed(), "Password field is not displayed"
    assert  menu_bar.is_displayed(),  "Button is not displayed"
    assert  text_header.is_displayed(), "Heading 'Test login' is not displayed"
    assert text_block.is_displayed(), "Login page description text is not displayed"
    assert full_text == expected_text, f"Text mismatch: {full_text}"
    assert submit_button.is_displayed() ,"Submit Button is missing "

@pytest.mark.positive
def test_valid_login(driver,login_elements):
    username,password,submit=login_elements
    username.send_keys("student")
    password.send_keys("Password123") 
    submit.click()
    assert driver.current_url=="https://practicetestautomation.com/logged-in-successfully/" , "invalid redirection"
    success_container=driver.find_element(By.XPATH, "//*[@id='loop-container']/div/article/div[1]/h1[contains(text(), 'Logged In Successfully')]")
    assert  success_container.is_displayed(), "Login failed"



 
@pytest.mark.negative
@pytest.mark.parametrize("username_input, password_input, expected_message", [
    ("incorrectUser", "Password123", "Incorrect login"),  # Test incorrect username
    ("student", "123", "Your password is invalid!"),     # Test incorrect password
    ("incorrectUser", "123", "Your username is invalid!")  # Test both incorrect
])
def test_invalid_login(driver, login_elements, username_input, password_input, expected_message):
    username, password, submit = login_elements
    username.send_keys(username_input)
    password.send_keys(password_input)
    submit.click()

    pop_up = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/section/section/div[2]'))
    )
    pop_up_message = pop_up.text
    assert pop_up_message == expected_message, f"Expected '{expected_message}', but got '{pop_up_message}'"     






@pytest.mark.positive
def  test_submit_button_activates(driver , login_elements):
    username, password, submit=login_elements
    username.send_keys("student")
    password.send_keys("Password123")
    assert  submit.is_enabled(),  "Submit button should be enabled after entering credentials"


@pytest.mark.negative
def test_submit_button_inactive_blank_fields(driver, login_elements):
    username, password, submit=login_elements
    username.clear()
    password.clear()
    assert not submit.is_enabled(),  "Submit button should be disabled when fields are empty"




@pytest.mark.negative
def test_submit_button_inactive_partial_input(driver, login_elements):
    username, password, submit=login_elements
    username.send_keys("student")
    password.clear()
    assert  not submit.is_enabled() , "Submit button should be disabled when only username is filled" 
    password.send_keys("Password123")
    username.clear()
    assert not submit.is_enabled(),  "Submit button should be disabled when  only  password is filled"





def  test_clicking_on_logo(driver):
    logo = driver.find_element(By.XPATH, '//*[@id="site-title"]/a/img')
    logo.click()

    assert driver.current_url=="https://practicetestautomation.com/", "invalid redirection"

