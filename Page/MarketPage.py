from selenium.webdriver.common.by import By

class Market():

    marketOptionMenuXpath = '//div[contains(text(), "Mercado")]'
    marketTitlePage = '//h4[contains(text(), "Mercado")]'

    def driverMarketPage(self, driver):
        self.base = driver

    def clickMarketButton(self):
        self.base.waitForTheElementToBePresent(By.XPATH, self.marketOptionMenuXpath)
        self.base.click(By.XPATH, self.marketOptionMenuXpath)

    def verifyPageMarket(self):
        self.base.waitForTheElementToBePresent(By.XPATH, self.marketTitlePage)