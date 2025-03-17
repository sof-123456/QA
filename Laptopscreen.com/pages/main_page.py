
from venv import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
from PIL import Image
from locators import *
import time
import logging

logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self,driver):
        self.driver=driver


    def wait_for_elements(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_locator_type(self, locator):
        if isinstance(locator, str): 
            if   locator.startswith('/'): 
                return By.XPATH   
            else:      
                return By.ID  
            
    def find_element_(self, locator):
            by=self.get_locator_type(locator)  
            return self.driver.find_element(by, locator)
    

    def click(self, locator):
        element=self.find_element_(locator)
        return element.click() 
    

    def write_to_search(self,locator,text):
         element=self.find_element_(locator)
         element.clear()
         element.send_keys(text)

    def screenshot_element(self, locator):
         element=self.find_element_(locator)
         element.screenshot("logo.jpg")

    def change_language(self,language):
        self.click(LANGUAGES_BUTTON)
        element=self.find_element_(language)
        element.click()
        time.sleep(3)
        
    def  convert_text_to_number(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((self.get_locator_type(locator), locator))) # type: ignore
        text =element.text
        cleaned_text = re.sub(r"[^\d.]", "", text)
        if not cleaned_text:
                logger.info(f"Element found with locator: {locator} ")
                raise ValueError(f"No numeric value found in element text: {text}")
        return float(cleaned_text) if "." in cleaned_text else int(cleaned_text) 
   

    def navigate_to(self, locator):
       self.driver.get(locator) 
       
