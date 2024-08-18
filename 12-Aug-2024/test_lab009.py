import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://app.vwo.com/#/login"
free_trail_url = "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"


@pytest.mark.postive
@allure.title("TC#1 Login to VWO - and free trail")
@allure.description("Test Description: Login to VWO and free trail")
def test_login_vwo_login_and_free_trail():
    driver = webdriver.Chrome()
    driver.get(url)

    user_name = driver.find_element(By.ID, "login-username")
    user_name.send_keys("Vijay")
    password = driver.find_element(By.CSS_SELECTOR, "[data-qa='jobodapuxe']")
    password.send_keys("Vijay@123")
    time.sleep(10)
    login_button = driver.find_element(By.ID, "js-login-btn")
    login_button.click()

    time.sleep(3)

    error_message_web_element = driver.find_element(By.CSS_SELECTOR, "[class='notification-box-description']")
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"

    time.sleep(3)

    # free_trail_web_element = driver.find_element(By.LINK_TEXT, "Start a free trial")
    free_trail_web_element = driver.find_element(By.PARTIAL_LINK_TEXT, "Start a free")
    free_trail_web_element.click()

    assert driver.current_url == free_trail_url
    time.sleep(3)
