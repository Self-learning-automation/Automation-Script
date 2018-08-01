from features import Locator


#must use from an instance. So where can I put my instance of Browser???
# browser = Browser()?????
class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_signin(self):
        return self.driver.find_element(Locator.sign_in[0], Locator.sign_in[1])

    def get_product1(self):
        return self.driver.find_element(Locator.product1[0], Locator.product1[1])

    def click_signin(self):
        self.get_signin().click()
