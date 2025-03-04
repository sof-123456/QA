import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure
from datetime import datetime
import os
import time
from selenium.common.exceptions import NoSuchElementException


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



def scroll_until_element_visible(driver, by, value, max_scrolls=0):
    for _ in range(max_scrolls):
        try:
            element = driver.find_element(by, value)
            if element.is_displayed():
                driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
                return element
        except NoSuchElementException:
            driver.execute_script("window.scrollBy(0, 500);")  
            time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")
            raise e

    raise Exception("Element not found after scrolling!")





@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_dir = "screenshots"
       
    try:
        os.makedirs(screenshot_dir, exist_ok=True) 
    except Exception as e:
        print(f"Failed to create folder: {e}")
        raise e
    

    if report.when == "call" and report.failed and "driver" in item.funcargs:
        driver = item.funcargs["driver"]
        element_id = "submit" 

        try:
            scroll_until_element_visible(driver, By.ID, element_id)
            screenshot_path = os.path.join(screenshot_dir, f"{element_id}_found_{timestamp}.png")
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot of element found: {screenshot_path}")
      
            with open(screenshot_path, "rb") as image_file:
             allure.attach(image_file.read(), name=f"{element_id}_found", attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            driver.execute_script("window.scrollTo(0, 0);")
            screenshot_path = os.path.join(screenshot_dir, f"{element_id}_error_{timestamp}.png")
            driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image_file:
                allure.attach(image_file.read(), name=f"{element_id}_error", attachment_type=allure.attachment_type.PNG)

            

       
