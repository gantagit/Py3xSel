import time

import allure
import pytest
from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from allure_commons.types import AttachmentType

url = "https://katalon-demo-cura.herokuapp.com/"
login_url = "https://katalon-demo-cura.herokuapp.com/profile.php#login"
error_text = "Login failed! Please ensure the username and password are valid."


@pytest.mark.postive
def test_login_katalon_cura():
    driver = webdriver.Chrome()
    driver.get(url)

    make_appointment = driver.find_element(By.ID, value="btn-make-appointment")
    make_appointment.click()

    Wait(driver=driver, timeout=5).until(EC.url_matches(login_url))
    assert driver.current_url == login_url

    username_web_element = driver.find_element(By.XPATH, "//input[@name='username']")
    password_web_element = driver.find_element(By.XPATH, "//input[@name='password']")
    login_web_element = driver.find_element(By.XPATH, "//button[text()='Login']")

    username_web_element.send_keys("Vijay")
    password_web_element.send_keys("Vijay")
    allure.attach(driver.get_screenshot_as_png(), name="login_details")
    login_web_element.click()


    # Explicit wait
    # Wait(driver=driver,
    #      timeout=5).until(
    #     EC.visibility_of_element_located((By.XPATH, "//p[@class='lead text-danger']")))

    # fluent wait
    ignored_list = [ElementNotVisibleException, ElementNotSelectableException]

    Wait(driver=driver,
         poll_frequency=1,
         timeout=5,
         ignored_exceptions=ignored_list).until(
        EC.visibility_of_element_located((By.XPATH, "//p[@class='lead text-danger']")))

    error_messages_web_element = driver.find_element(By.XPATH, "//p[@class='lead text-danger']")
    print(error_messages_web_element.text)

    allure.attach(driver.get_screenshot_as_png(), name="login_error_message", attachment_type=AttachmentType.PNG)
    assert error_messages_web_element.text == error_text
