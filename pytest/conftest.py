import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")  
    driver = webdriver.Chrome(options=chrome_options)
    # driver=webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    yield driver
    driver.quit()



@pytest.fixture
def login_elements(driver):
    username = driver.find_element(By.XPATH, '//*[@id="username"]')
    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    submit_button = driver.find_element(By.XPATH, '//*[@id="submit"]')
    return username, password, submit_button
