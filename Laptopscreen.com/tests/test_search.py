from   pages.main_page  import BasePage
import pytest
from locators import *
from  data import * 
import time


@pytest.mark.negative
def test_blanksearch(driver):
    main_page=BasePage(driver)
    main_page.find_element_(SEARCH).clear()
    main_page.click(GO_BUTTON)
    element=main_page.find_element_(BLANK_SEARCH)
    assert element.text==blank_search_text ,  "not currect text"


    

     