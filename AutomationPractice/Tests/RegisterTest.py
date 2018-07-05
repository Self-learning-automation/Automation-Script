from selenium.webdriver.common.by import By
import time;
from Config.Environment import Enviroment
from Pages.CreateAccountPage import CreateAccount
from Pages.HomePage import HomePage
from Pages.AuthencationPage import Authencation
from ultilities.Random import Random


class TestRegister(Enviroment):
    def test_Register(self):
        driver = self.driver
        #    1. Go to http://automationpractice.com/index.php page
        driver.get("http://automationpractice.com/index.php")
        lp = HomePage(driver)
        at = Authencation(driver)
        ct = CreateAccount(driver)
        rd = Random()
        #    2. Click on sign in button.
        lp.clickSignin()
        #    3. Input email address into Email address field .
        #    4. Click on create an account button.
        at.enterCreateEmailField("Tuanbui"+str(int(round(time.time() * 1000)))+"@gmail.com")
        at.clickCreateButton()
        #    5. Fill all personal information.
        #    6. Click on register button.
        ct.CreateAccountFlow(rd.randomString(8), rd.randomString(8), rd.randomString(8), rd.randomString(5), rd.randomString(6), rd.randomString(6),  rd.randomString(6),  rd.randomString(6),
                             rd.randomString(6), "12345",  rd.randomString(6), "0909090909",  rd.randomString(6))
