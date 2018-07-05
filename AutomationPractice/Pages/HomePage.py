import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

import Locator
from Config.Environment import Enviroment


class HomePage():
    def __init__(self, driver):
        self.driver = driver

    def getSignin(self):
        return self.driver.find_element(Locator.sign_in[0], Locator.sign_in[1])

    def clickSignin(self):
        self.getSignin().click()