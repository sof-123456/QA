import pytest
from pages.main_page import BasePage
from locators import * 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import re

logger = logging.getLogger(__name__)

def get_current_currency(driver):
    driver.execute_script("window.open('https://wise.com/gb/currency-converter/usd-to-cad-rate?amount=1000', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])
    my_driver = BasePage(driver)
    result=my_driver.convert_text_to_number(CURRENT_CURRENCY)
    driver.close()  
    driver.switch_to.window(driver.window_handles[0])  
    return result
    

def test_currency(driver):
    my_driver = BasePage(driver)
    current_currency = get_current_currency(my_driver.driver)
    my_driver.click(TOOLS_BUTTON)
    price_by_usd=my_driver.convert_text_to_number(PRICE)
    price_by_cad_real=current_currency*price_by_usd
    my_driver.click(CAD_BUTTON)
    price_by_cad=my_driver.convert_text_to_number(PRICE)
    assert price_by_cad==price_by_cad_real, f"no currect convertion  {price_by_cad} != {price_by_cad_real}"




def test_QTY(driver):

        my_driver=BasePage(driver)
        my_driver.navigate_to(URL_USD)
        price=my_driver.convert_text_to_number(PRICE)
        qty_1= my_driver.convert_text_to_number(QTY_1)
        assert  qty_1 == price , f"no match between {qty_1} and {price}" 
        qty_values=[
            my_driver.convert_text_to_number(QTY_2),
            my_driver.convert_text_to_number(QTY_10_MORE),
            my_driver.convert_text_to_number(QTY_100_MORE)
        ]
        for   i , qty_value in enumerate(qty_values):
            assert qty_value== qty_1 -(i+1), f"no match between   {qty_value} and {qty_1 -(i+1)} "
        