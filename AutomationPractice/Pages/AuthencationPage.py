import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Locator


class Authencation():
    def __init__(self, driver):
        self.driver = driver

    def getCreateEmailFiled(self):
        return self.driver.find_element(Locator.create_email_field[0], Locator.create_email_field[1])
    def getCreateBtn(self):
        return self.driver.find_element(Locator.caa_btn[0], Locator.caa_btn[1])
    def enterCreateEmailField(self, email):
        self.getCreateEmailFiled().send_keys(email)
    def clickCreateButton(self):
        self.getCreateBtn().click()
