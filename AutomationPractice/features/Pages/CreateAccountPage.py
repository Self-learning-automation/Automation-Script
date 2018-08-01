from hamcrest import equal_to, assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.Random import Random
from features import Locator
from features.browsers.browser import Browser


class CreateAccount(Browser):
    rd = Random()

    def __init__(self, driver):
        self.driver = driver

    ### Create Element
    def get_gender_male_btn(self):
        gender_male = Locator.gender_male
        return self.driver.find_element(gender_male[0], gender_male[1])

    def get_gender_female_btn(self):
        gender_female = Locator.gender_female
        return self.driver.find_element(gender_female[0], gender_female[1])

    def get_first_name_field(self):
        firstname_field = Locator.firstname_field
        return self.driver.find_element(firstname_field[0], firstname_field[1])

    def get_last_name_field(self):
        lastname_filed = Locator.lastname_filed
        return self.driver.find_element(lastname_filed[0], lastname_filed[1])

    def get_password_field(self):
        password_field = Locator.password_field
        return self.driver.find_element(password_field[0], password_field[1])

    def get_date_dropdown(self):
        date_dropdown = Locator.date_dropdown
        return self.driver.find_element(date_dropdown[0], date_dropdown[1])

    def get_month_dropdown(self):
        month_dropdown = Locator.month_dropdown
        return self.driver.find_element(month_dropdown[0], month_dropdown[1])

    def get_year_dropdown(self):
        year_dropdown = Locator.year_dropdown
        return self.driver.find_element(year_dropdown[0], year_dropdown[1])

    def get_cus_first_name(self):
        cus_firstname_field = Locator.cus_firstname_field
        return self.driver.find_element(cus_firstname_field[0], cus_firstname_field[1])

    def get_cus_last_name(self):
        cus_lastname_field = Locator.cus_lastname_field
        return self.driver.find_element(cus_lastname_field[0], cus_lastname_field[1])

    def get_cus_company_name(self):
        cus_company_field =Locator.cus_company_field
        return self.driver.find_element(cus_company_field[0], cus_company_field[1])

    def get_address(self):
        cus_address1_field = Locator.cus_address1_field
        return self.driver.find_element(cus_address1_field[0], cus_address1_field[1])

    def get_address_line2(self):
        cus_address2_field = Locator.cus_address2_field
        return self.driver.find_element(cus_address2_field[0], cus_address2_field[1])

    def get_city(self):
        cus_city_field = Locator.cus_city_field
        return self.driver.find_element(cus_city_field[0], cus_city_field[1])

    def get_state(self):
        cus_state_dropdown = Locator.cus_state_dropdown
        return self.driver.find_element(cus_state_dropdown[0], cus_state_dropdown[1])

    def get_post_code(self):
        cus_postcode_field = Locator.cus_postcode_field
        return self.driver.find_element(cus_postcode_field[0], cus_postcode_field[1])

    def get_additional_information(self):
        cus_additional_field = Locator.cus_additional_field
        return self.driver.find_element(cus_additional_field[0], cus_additional_field[1])

    def get_home_phone(self):
        cus_homephone = Locator.cus_homephone
        return self.driver.find_element(cus_homephone[0], cus_homephone[1])

    def get_mobile_phone(self):
        cus_mobiphone_field = Locator.cus_mobiphone_field
        return self.driver.find_element(cus_mobiphone_field[0], cus_mobiphone_field[1])

    def get_alias(self):
        cus_allias = Locator.cus_allias
        return self.driver.find_element(cus_allias[0], cus_allias[1])

    def get_register_btn(self):
        register_btn = Locator.register_btn
        return self.driver.find_element(register_btn[0], register_btn[1])

    ###Interactive

    def click_gender_male(self):
        self.get_gender_male_btn().click()

    def click_gender_female(self):
        self.get_gender_female_btn().click()

    def enter_first_name_field(self, name):
        self.get_first_name_field().clear()
        self.get_first_name_field().send_keys(name)

    def enter_last_name_field(self, name):
        self.get_last_name_field().clear()
        self.get_last_name_field().send_keys(name)

    def enter_password_field(self, password):
        self.get_password_field().send_keys(password)

    def choose_date_dropdown(self):
        select = Select(self.get_date_dropdown())
        select.select_by_value(str(self.rd.randomNumber(1, 31)))

    def choose_month_dropdown(self):
        select = Select(self.get_month_dropdown())
        select.select_by_value(str(self.rd.randomNumber(1, 12)))

    def choose_year_dropdown(self):
        select = Select(self.get_year_dropdown())
        select.select_by_value(str(self.rd.randomNumber(1900, 2018)))

    def enter_cus_first_name_field(self, name):
        self.get_cus_first_name().send_keys(name)

    def enter_cus_last_name_field(self, name):
        self.get_cus_last_name().send_keys(name)

    def enter_company_field(self, company):
        self.get_cus_company_name().send_keys(company)

    def enter_address_line1_field(self, address):
        self.get_address().send_keys(address)

    def enter_address_line2_field(self, address):
        self.get_address_line2().send_keys(address)

    def enter_city_field(self, city):
        self.get_city().send_keys(city)

    def choose_state_dropdown(self):
        select = Select(self.get_state())
        select.select_by_index(self.rd.randomNumber(1, 10))

    def enter_post_code(self, number):
        self.get_post_code().send_keys(number)

    def enter_additional_field(self, p):
        self.get_additional_information().send_keys(p)

    def enter_phone_number(self, number):
        self.get_mobile_phone().send_keys(number)

    def enter_home_phone_number(self, number):
        self.get_home_phone().send_keys(number)

    def enter_alias(self, text):
        self.get_alias().clear()
        self.get_alias().send_keys(text)

    def click_register_btn(self):
        self.get_register_btn().click()

    # Test Script
    def create_account_flow(self, firstname, lastname, password, cusFirstname, cusLastname, company, address1, address2,
                            city, postcode, additionalText, phone, alias):
        # Click on Gender
        self.click_gender_male()
        self.enter_first_name_field(firstname)
        self.enter_last_name_field(lastname)
        self.enter_password_field(password)
        self.choose_date_dropdown()
        self.choose_month_dropdown()
        self.choose_year_dropdown()
        self.enter_cus_first_name_field(cusFirstname)
        self.enter_cus_last_name_field(cusLastname)
        self.enter_company_field(company)
        self.enter_address_line1_field(address1)
        self.enter_address_line2_field(address2)
        self.enter_city_field(city)
        self.enter_post_code(postcode)
        self.choose_state_dropdown()
        self.enter_additional_field(additionalText)
        self.enter_phone_number(phone)
        self.enter_alias(alias)
        self.click_register_btn()
    def verify_register_successfully(self):
        expected_result = "Welcome to your account. Here you can manage all of your personal information and orders."
        actual_result = self.driver.find_element(By.CSS_SELECTOR, 'p.info-account').text
        assert_that(actual_result, equal_to(expected_result), 'Verify Message')