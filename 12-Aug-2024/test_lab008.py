import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://katalon-demo-cura.herokuapp.com/"
login_url = "https://katalon-demo-cura.herokuapp.com/profile.php#login"


@pytest.mark.postive
@allure.title("TC#1 Login to Katalon - Invalid Credentials")
@allure.description("Test Description: Login to Katalon with In-valid credentials")
def test_login_katalon_cura():
    driver = webdriver.Chrome()
    driver.get(url)
    make_appointment = driver.find_element(By.ID, value="btn-make-appointment")
    make_appointment.click()
    time.sleep(3)

    assert driver.current_url == login_url
    user_name = driver.find_element(By.NAME, "username")
    user_name.send_keys("Vijay")
    password = driver.find_element(By.CSS_SELECTOR, "[type='password']")
    password.send_keys("Vijay@123")
    time.sleep(3)
    login_button = driver.find_element(By.ID, "btn-login")
    login_button.click()
    time.sleep(3)
    error_message_web_element = driver.find_element(By.CSS_SELECTOR, "[class='lead text-danger']")
    assert error_message_web_element.text == "Login failed! Please ensure the username and password are valid."

    # < input
    # type = "text"
    # class ="form-control"
    # id="txt-username"
    # name="username"
    # placeholder="Username"
    # value="" autocomplete="off"
    # >

    # <p
    # class="lead text-danger">Login failed! Please ensure the username and password are valid.
    # </p>
    time.sleep(10)
