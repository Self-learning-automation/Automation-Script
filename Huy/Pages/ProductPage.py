from Pages import HomePage_Elements, RegisterPage_Elements, Product_Elements
from Common.CommonFunctions import Common
from selenium import webdriver
from selenium.webdriver.common.by import By
from hamcrest import *
import time
class ProductPage():
    def __init__(self, driver):
        self.driver = driver

    def VerifyAddToCart_Checkout(self):
        self.driver.find_element(Product_Elements.addtocart_CSS_Path[0], Product_Elements.addtocart_CSS_Path[1]).click()
        time.sleep(5)
        actual_SuccessfullyMessage = self.driver.find_element(Product_Elements.actual_SuccessfullyMessage[0],
                                                  Product_Elements.actual_SuccessfullyMessage[1]).text
        expected_Product_Name = self.driver.find_element(Product_Elements.expected_Product_Name[0],
                                                         Product_Elements.expected_Product_Name[1]).text
        expected_Page_Name = self.driver.find_element(Product_Elements.expected_Page_Name[0],
                                                      Product_Elements.expected_Page_Name[1]).text
        expected_Message = 'Success: You have added ' + expected_Product_Name + ' to your ' + expected_Page_Name + '!'
        assert_that(actual_SuccessfullyMessage, expected_Message)
        print("Added to cart successfully !")

        self.driver.find_element(Product_Elements.shoppingcartButton_CSS_Path[0],Product_Elements.shoppingcartButton_CSS_Path[1]).click()
        self.driver.find_element(Product_Elements.checkoutLink_CSS_Path[0],
                                 Product_Elements.checkoutLink_CSS_Path[1]).click()
        self.driver.find_element(Product_Elements.checkoutButton_CSS_Path[0],
                                 Product_Elements.checkoutButton_CSS_Path[1]).click()

        actual_NotAvailableMessage = self.driver.find_element(Product_Elements.alert_NotAvailableMessage[0],
                                                              Product_Elements.alert_NotAvailableMessage[1]).text
        expected_NotAvailable = ' Products marked with *** are not available in the desired quantity or not in stock!'

        assert_that(actual_NotAvailableMessage, expected_NotAvailable)
        print("Product is not available, checkout is failed !!!")








