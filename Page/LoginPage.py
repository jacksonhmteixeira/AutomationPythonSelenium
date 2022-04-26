from selenium import webdriver
from Base.SeleniumWebdriver import Base
from selenium.webdriver.common.by import By

class Login():

    emailFieldId = 'email'
    passwordFieldId = 'senha'
    enterButtonId = 'buttonLogin'
    toastContainerId = 'toast-container'
    buttonVisualizarProdutosId = "buttonVisualizarProdutos"
    messageRequiredLoginXpath = '//small[contains(text(),"E-mail é obrigatorio!")]'
    messageRequiredPasswordXpath = '//small[contains(text(), "Senha é obrigatório!")]'

    def openBrowserLogin(self):
        self.base = Base(driver=webdriver)
        self.base.openBrowser()

    def fillEmail(self, fieldValue):
        self.base.fillFieldId(self.emailFieldId, fieldValue)

    def fillPassword(self, fieldValue):
        self.base.fillFieldId(self.passwordFieldId, fieldValue)

    def clickEnterButton(self):
        self.base.click(self.enterButtonId)

    def verifyErrorMessage(self, text):
        self.base.waitForTheTextToBePresent(By.ID, self.toastContainerId, text)

    def verifyPageDashBoard(self):
        self.base.waitForTheElementToBePresent(By.ID, self.buttonVisualizarProdutosId)

    def verifyRequiredFieldLogin(self, text):
        self.base.waitForTheTextToBePresent(By.XPATH, self.messageRequiredLoginXpath, text)

    def verifyRequiredFieldPassWord(self, text):
        self.base.waitForTheTextToBePresent(By.XPATH, self.messageRequiredPasswordXpath, text)