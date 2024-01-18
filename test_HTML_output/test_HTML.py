

import path
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
from webdriver_manager.chrome import ChromeDriverManager
import time


def setup_module():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")

def teardown_module():
    driver.quit()

def test_googlename():
    assert driver.title == "Google"

def test_googleurl():
    assert driver.current_url == "hhhttps://www.google.com/"

# py.test -v -s --html=test_HTML_report.html

# Above is to generate the html report