from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitles = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkoutButtonLocator = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def getcardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitles)

    def getcardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def getcheckoutButton(self):
        self.driver.find_element(*CheckoutPage.checkoutButtonLocator).click()
        confirm = ConfirmPage(self.driver)
        return confirm


