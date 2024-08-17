import time

from selenium import webdriver

url = "https://app.vwo.com"


def test_vwo_login():
    driver = webdriver.Chrome()
    driver.get(url)
    # assert driver.title == "Login - "
    print(driver.title)
    assert driver.title == "Login - VWO"
    time.sleep(10)
