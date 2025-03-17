from pages.main_page import BasePage
import pytest
from locators import *
from visual_comparison.utiles import ImageComparisonUtil



@pytest.mark.positive
def test_logo(driver):
    main_page=BasePage(driver)
    logo_screen=main_page.screenshot_element(PAGE_LOGO)
    match_result = ImageComparisonUtil.check_match("logo.jpg","tests\expected_logo.png")

    assert match_result , "logos not match  "
