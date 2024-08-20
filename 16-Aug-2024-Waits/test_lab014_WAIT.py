import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

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
    login_web_element.click()

    Wait(driver=driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='lead text-danger']")))

    error_messages_web_element = driver.find_element(By.XPATH, "//p[@class='lead text-danger']")
    assert error_messages_web_element.text == error_text

