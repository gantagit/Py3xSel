import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://katalon-demo-cura.herokuapp.com/"


def test_book_appointment():
    driver = webdriver.Chrome()
    driver.get(url)
    make_appointment = driver.find_element(By.ID, value="btn-make-appointment")
    make_appointment.click()

    user_name = driver.find_element(By.NAME, "username")
    user_name.send_keys("Vijay")
    password = driver.find_element(By.NAME, "password")
    password.send_keys("Vijay@123")
    login_button = driver.find_element(By.CLASS_NAME, "btn btn-default")
    login_button.click()
    time.sleep(10)
