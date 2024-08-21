import time

import allure
import pytest
from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from allure_commons.types import AttachmentType

url = "https://katalon-demo-cura.herokuapp.com/"
login_url = "https://katalon-demo-cura.herokuapp.com/profile.php#login"
error_text = "Login failed! Please ensure the username and password are valid."


@pytest.mark.postive
def test_vwo_login_select():
    driver = webdriver.Chrome()
    driver.get(url)

