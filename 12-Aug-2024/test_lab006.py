import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://katalon-demo-cura.herokuapp.com/"
login_url = "https://katalon-demo-cura.herokuapp.com/profile.php#login"


@allure.title("Test Book Appointment")
@allure.description("Verify that user can book an appointment")
def test_book_appointment():
    driver = webdriver.Chrome()
    driver.get(url)
    make_appointment = driver.find_element(By.ID, value="btn-make-appointment")
    make_appointment.click()
    assert driver.current_url == login_url
    time.sleep(10)
