import time
from selenium.webdriver.chrome.options import Options

from selenium import webdriver

url = "https://app.vwo.com"


def test_vwo_login():

    chrome_options = Options()

    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--window-size=1920*1200")  # Specific Window Size
    chrome_options.add_argument("--incognito")  # Open Chrome in incognito mode
    # chrome_options.add_argument("--headless")  # Bypass OS security model
    driver = webdriver.Chrome(chrome_options)
    driver.get(url)
    time.sleep(10)