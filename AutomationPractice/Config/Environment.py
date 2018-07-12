import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait


class Enviroment(unittest.TestCase):
    def setUp(self):
        locationdriver = "/Users/tuanbuic/PycharmProjects/AutomationPractice/resources/chromedriver.exe"
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(locationdriver, chrome_options=opts)
        self.driver.implicitly_wait(10)
        self.driverdriver.maximize_window()

    def teardown(self):
        self.driver.quit()
