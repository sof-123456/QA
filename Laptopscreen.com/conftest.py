from selenium import webdriver 
import pytest
import logging


@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    driver.get("https://www.laptopscreen.com")
    driver.maximize_window()
    yield  driver
    driver.quit()


@pytest.fixture( autouse=True)
def setup_logging():
    
    logger = logging.getLogger()  
    logger.setLevel(logging.INFO)

    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
        
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    
    file_handler = logging.FileHandler('test_logs.log', mode='w')  
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)