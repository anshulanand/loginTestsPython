
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"


    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email,self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password,self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result =  self.isElementPresent("//*[@id='navbar']//span[text()='Test User']",
                                        locatorType="xpath")
        return result

    def verifyLoginFail(self):
        result =  self.isElementPresent("//div[contains(text(),'Invalid email or password')]",
                                        locatorType="xpath")
        return result

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

