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

alerts_url = "https://the-internet.herokuapp.com/javascript_alerts"
js_alert_locator = "//button[text()='Click for JS Alert']"
js_confirm_locator = "//button[text()='Click for JS Confirm']"
js_prompt_locator = "//button[text()='Click for JS Prompt']"
result_locator = "result"


class TestAlerts:

    @pytest.fixture(scope="class")
    def setup(self):
        options = Options()
        options.page_load_strategy = "normal"
        self.driver = webdriver.Chrome(options)
        yield  # return self.driver
        self.driver.quit()

    @pytest.mark.js_alerts
    @allure.description("TC#1 - Js Alert")
    @allure.description("Test case for Js Alert testing")
    def test_qa_tc1(self, setup):
        setup.get(alerts_url)
        js_alerts = self.driver.find_element(By.XPATH, js_alert_locator)
        js_alerts.click()
        time.sleep(3)
        allure.attach(driver=self.driver, name="JS Alert", attachment_type=AttachmentType.PNG)

        alert = Alert(self.driver)
        print(alert.text)
        alert.accept()

        result = self.driver.find_element(By.ID, result_locator)
        assert result == "You successfully clicked an alert"

    # @pytest.mark.js_confirm
    # @allure.description("TC#2 - Js Confirm")
    # @allure.description("Test case for Js Confirm testing")
    # def test_qa_tc2(self, setup):
    #     self.driver.get(alerts_url)
    #     js_alerts = self.driver.find_element(By.XPATH, js_confirm_locator)
    #     js_alerts.click()
    #     time.sleep(3)
    #     allure.attach(driver=self.driver, name="JS Confirm", attachment_type=AttachmentType.PNG)
    #
    #     alert = Alert(self.driver)
    #     print(alert.text)
    #     alert.accept()
    #
    #     result = self.driver.find_element(By.ID, result_locator)
    #     assert result == "You clicked: Ok"
    #
    # @pytest.mark.js_prompt
    # @allure.description("TC#3 - Js Prompt")
    # @allure.description("Test case for Js Prompt testing")
    # def test_qa_tc3(self, setup):
    #     self.driver.get(alerts_url)
    #     time.sleep(10)
    #     js_alerts = self.driver.find_element(By.XPATH, js_prompt_locator)
    #     js_alerts.click()
    #     time.sleep(3)
    #     allure.attach(driver=self.driver, name="JS Prompt", attachment_type=AttachmentType.PNG)
    #
    #     alert = Alert(self.driver)
    #     print(alert.text)
    #     alert.accept()
    #
    #     result = self.driver.find_element(By.ID, result_locator)
    #     assert result == "You entered: Vijay"
