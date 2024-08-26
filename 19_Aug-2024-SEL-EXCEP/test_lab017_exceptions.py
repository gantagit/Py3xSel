import os
import time
import pytest
import openpyxl
import allure
from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with as Locate
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.chrome.options import Options
from selenium.common import (StaleElementReferenceException)

vwo_login_url = "https://app.vwo.com/#/login"
username_locator = "//*[@id='login-username']"


def test_stale_element_exceptions():
    driver = webdriver.Chrome()
    driver.get(vwo_login_url)

    try:
        username = driver.find_element(By.XPATH, username_locator)
        driver.refresh() # Stale element exception due to refresh after the element found
        username.send_keys("gvk9786")
    except StaleElementReferenceException as sere:
        print(f" \n unable to find the element due to {sere}")
    finally:
        print("End of the program")

    driver.quit()
