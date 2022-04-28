from selenium.webdriver.common.by import By

class Market():

    marketOptionMenuXpath = '//div[contains(text(), "Mercado")]'
    marketTitlePage = '//h4[contains(text(), "Mercado")]'
    productSearchID = 'pesquisar_produto'
    productMonitor18 = '//h5[contains(text(), "Monitor 18 Polegadas")]'
    productTeclado = '//h5[contains(text(), "Teclado")]'
    productMouse = '//h5[contains(text(), "Mouse")]'
    productMonitor24 = '//h5[contains(text(), "Monitor 24")]'

    def driverMarketPage(self, driver):
        self.base = driver

    def clickMarketButton(self):
        self.base.waitForTheElementToBePresent(By.XPATH, self.marketOptionMenuXpath)
        self.base.click(By.XPATH, self.marketOptionMenuXpath)

    def verifyPageMarket(self):
        self.base.waitForTheElementToBePresent(By.XPATH, self.marketTitlePage)

    def fillProductSearch(self, text):
        self.base.fillFieldId(self.productSearchID, text)

    def checkProductPresented(self, product):
        match product:
            case 'Mouse':
                self.base.waitForTheElementToBePresent(By.XPATH, self.productMouse)
            case 'Monitor 18 Polegadas':
                self.base.waitForTheElementToBePresent(By.XPATH, self.productMonitor18)
            case 'Teclado':
                self.base.waitForTheElementToBePresent(By.XPATH, self.productTeclado)
            case 'Monitor 24" polegadas':
                self.base.waitForTheElementToBePresent(By.XPATH, self.productMonitor24)