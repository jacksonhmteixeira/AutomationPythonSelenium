from __future__ import unicode_literals, print_function
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

class Base():

    __baseURL = 'https://plataforma.engenheiroqa.com/#/login'

    def __init__(self, driver):
        self.driver = driver
        self.driver = webdriver.Chrome(os.getcwd() + ".\chromedriver.exe")

    def abrirNavegador(self):
        self.driver.maximize_window()
        self.driver.get(self.__baseURL)

    def clicar(self, identificacao):
        button = self.driver.find_element_by_id(identificacao)
        button.click()

    def preencherCampoID(self, identificacao, valorCampo):
        campo = self.driver.find_element_by_id(identificacao)
        campo.send_keys(valorCampo)

    def esperarAteAPresencaDoElemento(self, identificacao):
        self.esperar =  self.driver.find_element(By.ID, 'details-button')
        self.driver.wai
