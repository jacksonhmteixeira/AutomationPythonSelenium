from selenium import webdriver
from Base.SeleniumWebdriver import Base
from selenium.webdriver.common.by import By

class Product():

    productOptionMenuXpath = '//div[contains(text(), "Produtos")]'
    productTitlePage = '//h4[contains(text(), "Pesquisar Produto")]'

    def driverProductPage(self, driver):
        self.base = driver

    def clickProductButton(self):
        self.base.waitForTheElementToBePresent(By.XPATH, self.productOptionMenuXpath)
        self.base.click(By.XPATH, self.productOptionMenuXpath)

    def verifyPageProduct(self):
        self.base.waitForTheElementToBePresent(By.XPATH, self.productTitlePage)