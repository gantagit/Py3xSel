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
from selenium.common import (TimeoutException)

vwo_login_url = "https://app.vwo.com/#/login"
username_locator = "//*[@id='login-username']"  # No such element


def test_time_out_exceptions():
    driver = webdriver.Chrome()
    driver.get(vwo_login_url)

    try:
        username = driver.find_element(By.XPATH, username_locator)
        username.send_keys("gvk9786")
        Wait(driver=driver, timeout=5).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        )
    except TimeoutException as toe:
        print(f" \n unable to find element within wait time {toe}")
    finally:
        print("End of the program")

    driver.quit()
