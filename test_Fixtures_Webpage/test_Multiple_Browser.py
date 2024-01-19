# To run in parallel mode "py.test -n (Threads how many browsers)"

#py.test -n 4

import path
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_google_Chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    assert driver.title == "Google"
    driver.quit()

def test_goole_Firefox():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    assert driver.title == "Google"
    driver.quit()

