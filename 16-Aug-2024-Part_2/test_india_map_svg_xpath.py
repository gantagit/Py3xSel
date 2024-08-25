import time

import allure
import pytest
from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options

india_map_url = "https://www.amcharts.com/svg-maps/?map=india"
states = "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']"
preferred_state = "Tripura"


def test_india_map_states():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920*1200")  # Specific Window Size
    # chrome_options.add_argument("--incognito")  # Open Chrome in incognito mode
    # chrome_options.add_argument("--headless")  # Bypass OS security model
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.get(india_map_url)
    time.sleep(5)

    Wait(driver=driver, timeout=5).until(EC.url_contains(india_map_url))
    allure.attach(driver.get_screenshot_as_png(), name="india_map_states", attachment_type=AttachmentType.PNG)

    states_web_element = driver.find_elements(By.XPATH, states)
    for state in states_web_element:
        print(state.get_attribute("aria-label"))
        if preferred_state in state.get_attribute("aria-label"):
            state.click()
            allure.attach(driver.get_screenshot_as_png(), name=preferred_state, attachment_type=AttachmentType.PNG)
            break
    time.sleep(5)
