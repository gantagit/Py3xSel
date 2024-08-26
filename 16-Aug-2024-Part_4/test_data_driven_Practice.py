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
from selenium.common import ElementNotVisibleException, ElementNotSelectableException

vwo_login_url = "https://app.vwo.com/#/login"
vwo_dashboard_url = "https://app.vwo.com/#/dashboard"

username_locator = "//*[@name='username']"
password_locator = "//*[@id='login-password']"
login_button_locator = "//*[@id='js-login-btn']"
error_msg_locator = "//*[@id='js-notification-box-msg']"
# page_header_locator = ".page-heading"

# username = "admin@test.com"
# password = "pass123"
# username = "gvk9786@gmail.com"
# password = "Samarth@235"
error_msg = "Your email, password, IP address or location did not match"


def read_from_xlsx(file_path1):
    cred = []

    wb = openpyxl.load_workbook(file_path1)
    sh = wb.active

    for row in sh.iter_rows(min_row=2, values_only=True):
        username, password, status = row
        cred.append({
            "username": username,
            "password": password,
            "status": status
        })
    return cred


file_path = os.getcwd() + "/test_data.xlsx"
print(file_path)


@pytest.mark.parametrize("user_cred", read_from_xlsx(file_path1=file_path))
def test_vwo_login(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    status = user_cred["status"]
    # print(username + " | " + password + " | " + status)
    vwo_login(username1=username, password1=password)


def vwo_login(username1, password1):
    options = Options()
    # Add arguments to disable notifications and run in headless mode
    options.add_argument("--disable-notifications")
    # options.page_load_strategy = 'normal'
    # options.add_argument("--headless")
    # options.add_argument("--incognito")

    # Initialize the Chrome driver with the options
    driver = webdriver.Chrome(options)
    driver.get(vwo_login_url)

    Wait(driver=driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, login_button_locator)))

    username_web_element = driver.find_element(By.XPATH, username_locator)
    password_web_element = driver.find_element(By.XPATH, password_locator)
    login_button_web_element = driver.find_element(By.XPATH, login_button_locator)

    username_web_element.send_keys(username1)
    password_web_element.send_keys(password1)
    login_button_web_element.click()
    # Wait(driver=driver, timeout=10).until(
    #         driver.execute_script("return document.readyState") == "complete")
    time.sleep(5)

    if driver.current_url != vwo_dashboard_url:
        ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
        Wait(driver=driver, poll_frequency=1, timeout=60, ignored_exceptions=ignore_list).until(
            EC.visibility_of_element_located((By.XPATH, error_msg_locator)))
        error_msg_web_element = driver.find_element(By.XPATH, error_msg_locator)
        assert vwo_login_url in driver.current_url
        assert error_msg == error_msg_web_element.text
        allure.attach(driver.get_screenshot_as_png(), name=username1 + " invalid user credentials",
                      attachment_type=AttachmentType.PNG)
    # elif driver.current_url == vwo_dashboard_url:
    else:
        # Wait(driver=driver, timeout=10).until(EC.url_contains(vwo_dashboard_url))
        # Wait(driver=driver, poll_frequency=1, timeout=60, ignored_exceptions=ignore_list).until(
        #     EC.text_to_be_present_in_element((By.CSS_SELECTOR, page_header_locator), "Dashboard"))
        # Wait(driver=driver, timeout=10).until(
        #     driver.execute_script("return document.readyState") == "complete")
        allure.attach(driver.get_screenshot_as_png(), name=username1 + " Welcome to VWO",
                      attachment_type=AttachmentType.PNG)
    driver.quit()
