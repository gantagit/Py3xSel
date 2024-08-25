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

flipkart_url = "https://www.flipkart.com/"
svg_icon_xpath = "//*[local-name()='svg']/*[local-name()='path' and @stroke-linecap='round' and @d='M16 16L21 21']"
# svg_icon_xpath = "//*[local-name()='svg']/*[contains(text(),'Search Icon')]"
search_text_xpath = "//input[@name='q']"
search_for = "AC"
search_results_contains = "https://www.flipkart.com/search?q=AC"
search_results_url = "https://www.flipkart.com/search?q=AC"


def test_flipkart_svg():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920*1200")  # Specific Window Size
    chrome_options.add_argument("--incognito")  # Open Chrome in incognito mode
    # chrome_options.add_argument("--headless")  # Bypass OS security model

    driver = webdriver.Chrome(chrome_options)
    driver.get(flipkart_url)

    Wait(driver=driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, search_text_xpath)))
    search_text_web_element = driver.find_element(By.XPATH, value=search_text_xpath)
    search_text_web_element.send_keys(search_for)

    search_svg_element = driver.find_element(By.XPATH, value=svg_icon_xpath)
    search_svg_element.click()

    Wait(driver=driver, timeout=5).until(EC.url_contains(search_results_url))
    allure.attach(driver.get_screenshot_as_png(), name="search_results", attachment_type=AttachmentType.PNG)
    assert search_results_url in driver.current_url
