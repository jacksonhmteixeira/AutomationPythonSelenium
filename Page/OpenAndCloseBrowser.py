from selenium import webdriver
from Base.SeleniumWebdriver import Base

class OpenAndCloseBrowser():
    base = Base(driver=webdriver)

    def driverWebdriver(self):
        return self.base

    def openBrowser(self):
        self.driverWebdriver()
        self.base.openBrowser()

    def closeBrowser(self):
        self.base.closeBrowser()