import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("First Name is "+getData[0]["firstName"])
        homepage.getName().send_keys(getData[0]["firstName"])
        homepage.getEmail().send_keys(getData[0]["lastName"])
        homepage.getPassword().send_keys("12233dffff")
        homepage.getCheckbox().click()
        # Gender
        self.selectOptionByText(homepage.getGender(), getData[0]["gender"])
        # Employment Status
        homepage.getEmploymentStatus().click()
        # Submit-button
        homepage.submitForm().click()
        msg = homepage.getMessage().text
        log.info("Text received from application is " + msg)
        assert "Success!" in msg
        # Two-way data binding text-box
        homepage.getDataBindingText().send_keys(getData[0]["lastName"])
        self.driver.refresh()

    @pytest.fixture(params=[HomePageData.getTestData("Testcase2"), HomePageData.getTestData("Testcase3")])
    def getData(self, request):
        return request.param