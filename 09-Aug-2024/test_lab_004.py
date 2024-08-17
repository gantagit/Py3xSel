import time

import allure
from selenium.webdriver.chrome.options import Options

from selenium import webdriver

url = "https://app.vwo.com"


@allure.description("Test youtube with adblocker extension")
def test_vwo_page_source():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    print(driver.page_source)
    time.sleep(10)
