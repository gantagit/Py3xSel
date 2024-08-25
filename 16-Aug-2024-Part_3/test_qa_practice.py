import time

import allure
import pytest
from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with as Locate
from selenium.webdriver.support.ui import WebDriverWait as Wait
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options

qa_practice_url = "https://awesomeqa.com/practice.html"
years_of_experience = "//span[contains(text(),'Years of Experience')]"
preferred_years = "exp-2"


def test_qa_practice():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920*1200")  # Specific Window Size
    # chrome_options.add_argument("--incognito")  # Open Chrome in incognito mode
    # chrome_options.add_argument("--headless")  # Bypass OS security model
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.get(qa_practice_url)

    years_of_experience_web_element = driver.find_element(By.XPATH, years_of_experience)
    preferred_years_web_element = driver.find_element(Locate(By.ID, preferred_years).to_right_of(years_of_experience_web_element))
    preferred_years_web_element.click()

    allure.attach(driver.get_screenshot_as_png(), name=preferred_years, attachment_type=AttachmentType.PNG)

