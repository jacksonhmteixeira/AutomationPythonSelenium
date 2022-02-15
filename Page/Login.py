from selenium import webdriver
from Base.SeleniumWebdriver import Base

class Login():

    idCampoEmail = 'email'
    idCampoSenha = 'password'
    idBotaoEntrar = 'buttonLogin'

    def abrirNavegadorLogin(self):
        self.base = Base(driver=webdriver)
        self.base.abrirNavegador()

    def preencherEmail(self, valorCampo):
        self.base.preencherCampoID(self.idCampoEmail, valorCampo)

    def preencherSenha(self, valorCampo):
        self.base.preencherCampoID(self.idCampoSenha, valorCampo)

    def clicarBotaoEntrar(self):
        self.base.clicar(self.idBotaoEntrar)