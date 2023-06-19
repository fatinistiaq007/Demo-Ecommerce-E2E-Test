import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        # homePage.shopItems().click()
        checkout = homePage.shopItems()
        # checkout = CheckoutPage(self.driver)
        log.info("Getting all the card titles")
        elements = checkout.getcardTitles()
        # confirm = ConfirmPage(self.driver)
        i = -1
        for ele in elements:
            i = i + 1
            log.info(ele.text)
            if ele.text == "Blackberry":
                checkout.getcardFooter()[i].click()
        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirm = checkout.getcheckoutButton()
        time.sleep(5)
        # self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
        confirm.getcheckoutConfirm().click()
        # self.driver.find_element(By.ID, "country").send_keys("Bangla")
        log.info("Entering country name as bangla")
        confirm.getcountryName().send_keys("bangla")
        self.verifyLinkPresence("Bangladesh")

        # self.driver.find_element(By.CSS_SELECTOR, "div[class='suggestions'] ul li a").click()
        confirm.selectCountry().click()
        # self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        confirm.selectAgree().click()
        # self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        confirm.purchaseItem().click()
        # success = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        success = confirm.getPurchaseConfirmationText().text
        log.info("Text received from application is " + success)
        assert "Success! Thank you!" in success



