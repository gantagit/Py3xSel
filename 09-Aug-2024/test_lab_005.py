import time

import allure
from selenium.webdriver.chrome.options import Options

from selenium import webdriver

url = "https://app.vwo.com"


@allure.description("Test youtube with adblocker extension")
def test_close_and_quit():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    print(driver.page_source)
    driver.refresh()
    time.sleep(10)
    driver.back()
    time.sleep(10)
    driver.forward()
    time.sleep(10)
    driver.close()
    time.sleep(10)
    driver.quit()
