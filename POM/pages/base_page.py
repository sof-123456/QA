from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import re



class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_elements(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    

    def  find_element__(self, locator):
        find_by=[By.ID, By.XPATH,By.CLASS_NAME,By.NAME]
       
        try :
            return self.wait_for_elements((self.get_locator_type(locator),locator))
        except:

            raise NoSuchElementException(f"Element not found with locator '{locator}'  by {find_by}")      
    
    def send_keys(self, locator, text):
        element = self.find_element__(locator )
        element.clear()
        element.send_keys(text)


    def get_text(self, locator):
        element = self.find_element__(locator)
        return element.text

    def click(self, locator, by):
        element = self.find_element__(locator)
        element.click()

    def get_current_url(self):
        return self.driver.current_url
    
    def  get_locator_type(self, locator):
        if re.match("//*", locator):
            return By.XPATH
        else :
            return By.ID
         
        

    def scroll_until_element_visible(self,locator, max_scroll=10):
        for i in range(max_scroll):
            try: 
                element=self.find_element__(locator)
                if element.is_displayed():
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
            except NoSuchElementException:
                    self.driver.execute_script("window.scrollBy(0, 500);")  
                    time.sleep(1)
            except Exception as e:
                print(f"Error: {e}")
                raise e
        
