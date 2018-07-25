

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ultilities.Random import Random
import Locator
from features.browsers.browser import Browser


class CreateAccount(Browser):
    rd = Random()
    def __init__(self, driver):
        self.driver = driver
    ### Create Element
    def getGenderMaleBtn(self):
        return self.driver.find_element(Locator.gender_male[0], Locator.gender_male[1])

    def getGenderFemaleBtn(self):
        return self.driver.find_element(Locator.genter_femaile[0], Locator.genter_femaile[1])

    def getFirstNameField(self):
        return self.driver.find_element(Locator.firstname_field[0], Locator.firstname_field[1])

    def getLastNameField(self):
        return self.driver.find_element(Locator.lastname_filed[0], Locator.lastname_filed[1])

    def getPasswordField(self):
        return self.driver.find_element(Locator.password_field[0], Locator.password_field[1])

    def getDateDropdown(self):
        return self.driver.find_element(Locator.date_dropdown[0], Locator.date_dropdown[1])

    def getMonthDropdown(self):
        return self.driver.find_element(Locator.month_dropdown[0], Locator.month_dropdown[1])

    def getYearDropdown(self):
        return self.driver.find_element(Locator.year_dropdown[0], Locator.year_dropdown[1])

    def getCusFirstName(self):
        return self.driver.find_element(Locator.cus_firstname_field[0], Locator.cus_firstname_field[1])

    def getCusLastName(self):
        return self.driver.find_element(Locator.cus_lastname_field[0], Locator.cus_lastname_field[1])

    def getCusCompanyName(self):
        return self.driver.find_element(Locator.cus_company_field[0], Locator.cus_company_field[1])

    def getAddress(self):
        return self.driver.find_element(Locator.cus_address1_field[0], Locator.cus_address1_field[1])

    def getAddressLine2(self):
        return self.driver.find_element(Locator.cus_address2_field[0], Locator.cus_address2_field[1])

    def getCity(self):
        return self.driver.find_element(Locator.cus_city_field[0], Locator.cus_city_field[1])

    def getState(self):
        return self.driver.find_element(Locator.cus_state_dropdown[0], Locator.cus_state_dropdown[1])

    def getPostCode(self):
        return self.driver.find_element(Locator.cus_postcode_field[0], Locator.cus_postcode_field[1])

    def getAdditionalInformation(self):
        return self.driver.find_element(Locator.cus_additional_field[0], Locator.cus_additional_field[1])

    def getHomePhone(self):
        return self.driver.find_element(Locator.cus_homephone[0], Locator.cus_homephone[1])

    def getMobilePhone(self):
        return self.driver.find_element(Locator.cus_mobiphone_field[0], Locator.cus_mobiphone_field[1])

    def getAlias(self):
        return self.driver.find_element(Locator.cus_allias[0], Locator.cus_allias[1])

    def getRegisterBtn(self):
        return self.driver.find_element(Locator.register_btn[0], Locator.register_btn[1])

    ###Interactive

    def clickGenderMale(self):
        self.getGenderMaleBtn().click()

    def clickGenderFemale(self):
        self.getGenderFemaleBtn().click()

    def enterFirstnameField(self, name):
        self.getFirstNameField().clear()
        self.getFirstNameField().send_keys(name)

    def enterLastnameField(self, name):
        self.getLastNameField().clear()
        self.getLastNameField().send_keys(name)

    def enterPasswordField(self, password):
        self.getPasswordField().send_keys(password)

    def chooseDateDropdown(self):
        select = Select(self.getDateDropdown())
        select.select_by_value(str(self.rd.randomNumber(1,31)))

    def chooseMonthDropdown(self):
        select = Select(self.getMonthDropdown())
        select.select_by_value(str(self.rd.randomNumber(1,12)))

    def chooseYearDropdown(self):
        select = Select(self.getYearDropdown())
        select.select_by_value(str(self.rd.randomNumber(1900,2018)))

    def enterCusFirstnameField(self, name):
        self.getCusFirstName().send_keys(name)

    def enterCusLastnameField(self, name):
        self.getCusLastName().send_keys(name)

    def enterCompanyField(self, company):
        self.getCusCompanyName().send_keys(company)

    def enterAddressLine1Field(self, address):
        self.getAddress().send_keys(address)

    def enterAddressLine2Field(self, address):
        self.getAddressLine2().send_keys(address)

    def enterCityField(self, city):
        self.getCity().send_keys(city)

    def chooseStateDropdown(self):
        select = Select(self.getState())
        select.select_by_index(self.rd.randomNumber(1,10))

    def enterPostcode(self, number):
        self.getPostCode().send_keys(number)

    def chooseStateDropdown(self):
        select = Select(self.getState())
        select.select_by_index(self.rd.randomNumber(0,10))

    def enterAdditionalField(self, p):
        self.getAdditionalInformation().send_keys(p)

    def enterPhoneNumber(self, number):
        self.getMobilePhone().send_keys(number)

    def enterHomePhoneNumber(self, number):
        self.getHomePhone().send_keys(number)

    def enterAlias(self, text):

        self.getAlias().clear()
        self.getAlias().send_keys(text)

    def clickRegisterBtn(self):
        self.getRegisterBtn().click()
    #Test Script
    def CreateAccountFlow(self,firstname,lastname,password,cusFirstname,cusLastname,company,address1,address2,city,postcode,additionalText,phone,alias):
        # Click on Gender
        self.clickGenderMale()
        self.enterFirstnameField(firstname)
        self.enterLastnameField(lastname)
        self.enterPasswordField(password)
        self.chooseDateDropdown()
        self.chooseMonthDropdown()
        self.chooseYearDropdown()
        self.enterCusFirstnameField(cusFirstname)
        self.enterCusLastnameField(cusLastname)
        self.enterCompanyField(company)
        self.enterAddressLine1Field(address1)
        self.enterAddressLine2Field(address2)
        self.enterCityField(city)
        self.enterPostcode(postcode)
        self.chooseStateDropdown()
        self.enterAdditionalField(additionalText)
        self.enterPhoneNumber(phone)
        self.enterAlias(alias)
        self.clickRegisterBtn()