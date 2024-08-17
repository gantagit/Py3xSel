import time

import allure
from selenium.webdriver.chrome.options import Options

from selenium import webdriver

url = "https://www.youtube.com/watch?v=xns7fFro8qU"
chrome_downloads = "C:/Users/gvk97/Videos/Pramod Automation/chrome-extensions"


@allure.description("Test youtube with adblocker extension")
def test_youtube():
    chrome_options = Options()

    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_extension(f"{chrome_downloads}/Adblock.crx")  # Load Adblocker Extension# Specific Window Size
    chrome_options.add_argument("--page-load-strategy=normal")  # page load strategy
    # chrome_options.add_argument("--proxy-server=")  # specific proxy server
    driver = webdriver.Chrome(chrome_options)
    driver.get(url)
    driver.maximize_window()
    time.sleep(10)
