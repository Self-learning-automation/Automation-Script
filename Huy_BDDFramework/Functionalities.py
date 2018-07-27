import random
import string

from conf.env_setup import EnvSetup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CommonFunctionalities():
    def Click(self, locator, context):
        context.browser.find_element(locator).click()

    def Input_Text(self, locator, context, text):
        context.browser.find_element(locator).send_keys(text)

    def Get_Text(self, locator, context):
        return context.browser.find_element(locator).text

    def Random_Digits(length):
        return ''.join(random.choice(string.digits) for m in range(length))
