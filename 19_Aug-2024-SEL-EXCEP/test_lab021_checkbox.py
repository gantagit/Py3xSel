import os
import time
import pytest
import openpyxl
import allure
from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with as Locate
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.chrome.options import Options
from selenium.common import (TimeoutException)

checkbox_url = "https://the-internet.herokuapp.com/checkboxes"
checkbox_locator = "//input[@type='checkbox']"

class TestCheckbox:

    # @pytest.mark.js_alerts
    @allure.description("TC#1 - CheckBox")
    @allure.description("Test case for CheckBox testing")
    def test_qa_tc1(self):
        options = Options()
        options.page_load_strategy = "normal"
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options)
        self.driver.get(checkbox_url)

        checkbox_element = self.driver.find_elements(By.XPATH, checkbox_locator)
        checkbox_element[0].click()
        # allure.attach(webdriver=self.driver.get_screenshot_as_png(), name=checkbox_element[0].text,
        #               attachment_type=AttachmentType.PNG)
