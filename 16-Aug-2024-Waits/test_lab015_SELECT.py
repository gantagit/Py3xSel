import time

import allure
import pytest
from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from allure_commons.types import AttachmentType

from selenium.webdriver.support.ui import Select

url = "https://the-internet.herokuapp.com/dropdown"


@pytest.mark.postive
def test_vwo_login_select():
    driver = webdriver.Chrome()
    driver.get(url)

    choose_option = driver.find_element(By.ID, "dropdown")
    select_option = Select(choose_option)

    time.sleep(3)
    select_option.select_by_visible_text("Option 1")

    time.sleep(5)
