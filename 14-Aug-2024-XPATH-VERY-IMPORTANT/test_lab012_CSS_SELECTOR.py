import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://app.vwo.com/#/login"


@pytest.mark.postive
def test_login_katalon_cura():
    driver = webdriver.Chrome()
    driver.get(url)
    # // by using cssSelector
    # make_appointment = driver.find_element(By.CSS_SELECTOR, value="a#btn-make-appointment")
    # in cssSelector
    # id -> #id
    # class -> .class
    # div span = div.span

    # custom attributes in cssSelector
    make_appointment = driver.find_element(By.CSS_SELECTOR, value="input[data-qa='hocewoqisi']")
    # css token xpath and vice versa
    # a#btn-make-appointment -> //a[@id='btn-make-appointment']
    make_appointment.send_keys("Vijay")

    time.sleep(10)
