import time

from selenium.webdriver import ActionChains

from Config.Environment import Enviroment
from Pages.CreateAccountPage import CreateAccount
from Pages.HomePage import HomePage
from Pages.AuthencationPage import Authencation
from ultilities.Random import Random
import Locator

class TestBuying(Enviroment):
    def test_Buyflow(self):
        action = ActionChains(self.driver)
        self.driver.get("http://automationpractice.com/index.php")
        product1 = self.driver.find_element(Locator.product1[0],Locator.product1[1])
        product1_add = self.driver.find_element(Locator.product1_add_btn[0],Locator.product1_add_btn[1])
        action.move_to_element(product1).move_to_element(product1_add).click().perform()
