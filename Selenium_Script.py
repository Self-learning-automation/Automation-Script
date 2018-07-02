from selenium.webdriver.support.select import Select
import pytest
import datetime
from selenium import webdriver
import unittest
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Excercise_Test(unittest.TestCase):

    def setUp(self):
        # C:\Users\ASUS\PycharmProjects\SelfLearningAutomation\resource\chromedriver.exe
        locationdriver = "/Users/ASUS/PycharmProjects/SelfLearningAutomation/resource/chromedriver.exe"
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(locationdriver, chrome_options=opts)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])

    @pytest.mark.run(order=1)
    def test_Login(self):
        self.driver.get("http://automationpractice.com/")
        self.driver.find_element(By.CSS_SELECTOR, ".login").click()
        # tuancb123@gmail.com/tuancb
        # Enter Email address/password
        self.driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("tuancb123@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "input#passwd").send_keys("tuancb123")
        # click Sign in button
        self.driver.find_element(By.CSS_SELECTOR, "button#SubmitLogin").click()
        # Verify Login successfully
        actual_result = self.driver.find_element(By.CSS_SELECTOR, "p.info-account").text
        expected_result = "Welcome to your account. Here you can manage all of your personal information and orders."
        self.assertEqual(expected_result,actual_result)

    @pytest.mark.run(order=2)
    def test_register(self):
        self.driver.get("http://automationpractice.com/")
        # Click on Sign in
        self.driver.find_element(By.CSS_SELECTOR, ".login").click()
        # Input email address into Email address field .
        # Click on create an account button.
        self.driver.find_element(By.CSS_SELECTOR, "input#email_create").send_keys("abcderfefe3333@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "button#SubmitCreate").submit()
        # Fill all personal information.
        self.driver.find_element(By.CSS_SELECTOR, "input#id_gender1").click()
        self.driver.find_element(By.CSS_SELECTOR, "input#customer_firstname").send_keys("Tuan")
        self.driver.find_element(By.CSS_SELECTOR, "input#customer_lastname").send_keys("Bui")
        self.driver.find_element(By.CSS_SELECTOR, "input#passwd").send_keys("tuancb123")
        select = Select(self.driver.find_element(By.CSS_SELECTOR, "select#days"))
        select.select_by_index(1)
        select1 = Select(self.driver.find_element(By.CSS_SELECTOR, "select#months"))
        select1.select_by_index(1)
        select2 = Select(self.driver.find_element(By.CSS_SELECTOR, "select#years"))
        select2.select_by_index(1)
        self.driver.find_element(By.CSS_SELECTOR, "input#firstname").send_keys("Tuan")
        self.driver.find_element(By.CSS_SELECTOR, "input#lastname").send_keys("Bui")
        self.driver.find_element(By.CSS_SELECTOR, "input#company").send_keys("Nashtech")
        self.driver.find_element(By.CSS_SELECTOR, "input#address1").send_keys("Etown Cong Hoa")
        self.driver.find_element(By.CSS_SELECTOR, "input#city").send_keys("HCM")
        select3 = Select(self.driver.find_element(By.CSS_SELECTOR, "select#id_state"))
        select3.select_by_index(1)
        self.driver.find_element(By.CSS_SELECTOR, "input#postcode").send_keys("12345")
        self.driver.find_element(By.CSS_SELECTOR, "input#phone_mobile").send_keys("090909090909")
        alias = self.driver.find_element(By.CSS_SELECTOR, "input#alias")
        alias.clear()
        alias.send_keys("Tuan Bui Cong")
        # click submit
        self.driver.find_element(By.CSS_SELECTOR, "button#submitAccount").click()
        # Verify Register successfully
        actual_result = self.driver.find_element(By.CSS_SELECTOR,"p.info-account").text
        expected_result = "Welcome to your account. Here you can manage all of your personal information and orders."
        self.assertEqual(actual_result,expected_result)
    #def test_Buying(self):


# def tearDown(self):
#     self.driver.quit()
