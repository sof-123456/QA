from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_elements(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def send_keys(self, locator, text):
        element = self.wait_for_elements(locator)
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait_for_elements(locator)
        return element.text

    def click(self, locator):
        element = self.wait_for_elements(locator)
        element.click()

    def get_current_url(self):
        return self.driver.current_url
    