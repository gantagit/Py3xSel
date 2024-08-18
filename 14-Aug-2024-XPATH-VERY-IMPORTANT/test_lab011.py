import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://katalon-demo-cura.herokuapp.com/"
login_url = "https://katalon-demo-cura.herokuapp.com/profile.php#login"


@pytest.mark.postive
def test_login_katalon_cura():
    driver = webdriver.Chrome()
    driver.get(url)

    # // by using (basic locators) id , name, className, tagName, linkText, partialLinkText
    # make_appointment = driver.find_element(By.ID, value="btn-make-appointment")

    # // by using (advance locators) cssSelector, XPATH

    # // by using Absolute XPATH (Full path from the root element)
    # make_appointment = driver.find_element(By.XPATH, value="/html/body/header/div/a")

    # // by using Relative XPATH (basic locators)
    # make_appointment = driver.find_element(By.XPATH, value="//a[@id='btn-make-appointment']")

    # XPATH functions ************************************************************************
    # // by using Relative XPATH (XPATH text() functions - exact match)
    # make_appointment = driver.find_element(By.XPATH, value="//a[text()='Make Appointment']")

    # // by using Relative XPATH (XPATH contains(text(), 'value' functions - partial match)
    # make_appointment = driver.find_element(By.XPATH, value="//a[contains(text(), 'Make App')]")

    # // by using Relative XPATH (XPATH starts-with(text(), 'value' functions - partial match)
    make_appointment = driver.find_element(By.XPATH, value="//a[starts-with(text(),'Make')]")
    # XPATH functions ************************************************************************

    make_appointment.click()

    time.sleep(10)
