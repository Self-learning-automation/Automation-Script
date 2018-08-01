from features import Locator
from features.browsers.browser import Browser


class Authencation(Browser):
    def __init__(self, driver):
        self.driver = driver

    def get_createemail_filed(self):
        return self.driver.find_element(Locator.create_email_field[0], Locator.create_email_field[1])

    def get_create_btn(self):
        return self.driver.find_element(Locator.caa_btn[0], Locator.caa_btn[1])

    def enter_createemail_field(self, email):
        self.get_createemail_filed().send_keys(email)

    def click_create_button(self):
        self.get_create_btn().click()
