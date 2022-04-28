from __future__ import unicode_literals, print_function
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class Base():

    __baseURL = 'https://plataforma.engenheiroqa.com/#/login'

    def __init__(self, driver):
        self.driver = driver
        self.driver = webdriver.Chrome(os.getcwd() + ".\chromedriver.exe")

    def openBrowser(self):
        self.driver.maximize_window()
        self.driver.get(self.__baseURL)

    def click(self, typeIdentification, elementIdentification):
        button = self.driver.find_element(typeIdentification, elementIdentification)
        button.click()

    def fillFieldId(self, elementIdentification, fieldValue):
        field = self.driver.find_element_by_id(elementIdentification)
        field.send_keys(fieldValue)

    def waitForTheElementToBePresent(self, typeIdentification, elementIdentification):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((typeIdentification, elementIdentification)))

    def waitForTheTextToBePresent(self, typeIdentification, elementIdentification, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.text_to_be_present_in_element((typeIdentification, elementIdentification), text))

    def closeBrowser(self):
        self.driver.close()