from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    checkoutConfirmLocator = (By.XPATH, "//button[normalize-space()='Checkout']")
    countrySelector = (By.ID, "country")
    countrySuggestion = (By.CSS_SELECTOR, "div[class='suggestions'] ul li a")
    agreedSelector = (By.XPATH, "//label[@for='checkbox2']")
    purchaseButton = (By.XPATH, "//input[@value='Purchase']")
    purchaseSuccessMessage = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def getcheckoutConfirm(self):
        return self.driver.find_element(*ConfirmPage.checkoutConfirmLocator)

    def getcountryName(self):
        return self.driver.find_element(*ConfirmPage.countrySelector)

    def selectCountry(self):
        return self.driver.find_element(*ConfirmPage.countrySuggestion)

    def selectAgree(self):
        return self.driver.find_element(*ConfirmPage.agreedSelector)

    def purchaseItem(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getPurchaseConfirmationText(self):
        return self.driver.find_element(*ConfirmPage.purchaseSuccessMessage)

