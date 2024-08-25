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

aqi_index_url = "https://www.aqi.in/real-time-most-polluted-city-ranking"
search_text_xpath = "//*[@id='search_city']"
preferred_country = "India"
list_of_states_xpath = "//table[@id='example']/tbody/tr/td[2]"


def test_qa_practice():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920*1200")  # Specific Window Size
    # chrome_options.add_argument("--incognito")  # Open Chrome in incognito mode
    # chrome_options.add_argument("--headless")  # Bypass OS security model
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.get(aqi_index_url)

    time.sleep(5)

    allure.attach(driver.get_screenshot_as_png(), name="list_of_states_before_Search",
                  attachment_type=AttachmentType.PNG)

    search_web_element = driver.find_element(By.XPATH, search_text_xpath)
    search_web_element.send_keys(preferred_country)

    time.sleep(10)
    # Wait(driver=driver, timeout=5).until(
    #     EC.visibility_of_element_located((By.XPATH, list_of_states_xpath)))

    list_of_states = driver.find_elements(By.XPATH, list_of_states_xpath)

    print("Name" + " | " + "Rank" + " | " + "AQI Index")

    for state in list_of_states:
        if "India" in state.text:
            rank = driver.find_element(Locate(By.TAG_NAME, "p").to_right_of(state))
            aqi = driver.find_element(Locate(By.TAG_NAME, "p").to_left_of(state))
            print(state.text + " | " + rank.text + " | " + aqi.text)

    allure.attach(driver.get_screenshot_as_png(), name="list_of_states_After_Search", attachment_type=AttachmentType.PNG)
