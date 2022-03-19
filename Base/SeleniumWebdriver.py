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

    def openBrowser(self):
        self.driver.maximize_window()
        self.driver.get(self.__baseURL)

    def click(self, elementIdentification):
        button = self.driver.find_element_by_id(elementIdentification)
        button.click()

    def fillFieldId(self, elementIdentification, fieldValue):
        field = self.driver.find_element_by_id(elementIdentification)
        field.send_keys(fieldValue)

    def waitForThePresentElement(self, elementIdentification):
        field = self.driver.find_element_by_id(elementIdentification)
