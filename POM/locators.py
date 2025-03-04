from selenium.webdriver.common.by import By

URL_LOGIN="https://practicetestautomation.com/practice-test-login/"


USERNAME=(By.ID,"username")
PASSWORD=(By.ID,"password")
SUBMIT=(By.ID,"submit")
ERROR_MESSAGE=(By.ID,"error")
SUCCESS_MESSAGE=(By.XPATH, '//*[@id="loop-container"]/div/article/div[1]/h1')

LOG_OUT=(By.XPATH,'//*[@id="loop-container"]/div/article/div[2]/div/div/div/a')  

