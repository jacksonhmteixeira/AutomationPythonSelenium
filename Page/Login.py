from selenium import webdriver
from Base.SeleniumWebdriver import Base

class Login():

    emailFieldId = 'email'
    passwordFieldId = 'senha'
    enterButtonId = 'buttonLogin'

    def openBrowserLogin(self):
        self.base = Base(driver=webdriver)
        self.base.openBrowser()

    def fillEmail(self, fieldValue):
        self.base.fillFieldId(self.emailFieldId, fieldValue)

    def fillPassword(self, fieldValue):
        self.base.fillFieldId(self.passwordFieldId, fieldValue)

    def clickEnterButton(self):
        self.base.click(self.enterButtonId)