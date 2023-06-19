from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[contains(@href,'shop')]")
    name = (By.XPATH, "(//input[@name='name'])[1]")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.CSS_SELECTOR, "#exampleCheck1")

    gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    employmentStatus = (By.CSS_SELECTOR, "#inlineRadio2")
    submit = (By.XPATH, "//input[@class='btn btn-success']")
    message = (By.CLASS_NAME, "alert-success")
    dataBindingTextbox = (By.CSS_SELECTOR, "input.ng-dirty")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckoutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getEmploymentStatus(self):
        return self.driver.find_element(*HomePage.employmentStatus)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getMessage(self):
        return self.driver.find_element(*HomePage.message)

    def getDataBindingText(self):
        return self.driver.find_element(*HomePage.dataBindingTextbox)










