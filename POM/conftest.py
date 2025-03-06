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


       
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    rep = outcome.get_result()
    print(rep.when)
    setattr(item,'rep_'+rep.when,rep)
    return rep


@pytest.fixture(autouse=True)
def make_screenshot(request,driver):
    yield
    if    request.node.rep_call.outcome=="failed":

           allure.attach(driver.get_screenshot_as_png(), name=f"found", attachment_type=allure.attachment_type.PNG)
