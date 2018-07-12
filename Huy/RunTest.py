from selenium import webdriver
import unittest
from hamcrest import *

from Pages import RegisterPage_Elements
from Pages.HomePage import HomePage


class RunTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/huyle/PycharmProjects/Automation/resources/chromedriver.exe")
        self.driver.maximize_window()

    def test_Register(self):
        self.driver.get("https://demo.opencart.com/index.php")
        test_HomePage = HomePage(self.driver)
        test_HomePage.Verify_Register_Successfully()
        actual_successfullyMessage = self.driver.find_element(
            RegisterPage_Elements.actual_successfullyMessage_XPath_Path[0],
            RegisterPage_Elements.actual_successfullyMessage_XPath_Path[
                1]).text
        expected_successfullyMessage = 'Congratulations! Your new account has been successfully created!'
        assert_that(actual_successfullyMessage, has_string(expected_successfullyMessage))
        print('Account is created successfully')
        continueButton2 = self.driver.find_element(RegisterPage_Elements.continueButton2_CSS_Path[0],
                                                   RegisterPage_Elements.continueButton2_CSS_Path[1]).click()
#   def tearDown(self):
#        self.driver.close()
# if __name__ == '__main__':
#     unittest.main()
