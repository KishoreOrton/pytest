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

def test_google():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    assert driver.title == "Google"
    driver.quit()

def test_facebook():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    assert driver.title == "facebook"
    driver.quit()

def test_instagram():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.instagram.com/")
    assert driver.title == "instagram"
    driver.quit()

def test_gmail():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get("https://www.gmail.com/")
    assert driver.title == "Gmail"
    driver.quit()

