from behave import *
from selenium.webdriver.common.by import By
from conf.env_setup import EnvSetup
from hamcrest import assert_that, equal_to
from common_functionalities.Functionalities import CommonFunctionalities
from pages.HomePageLocators import HomePageLocators
from pages.SignUpLocators import SignUpLocators
from pages.MyAccountLocators import MyAccountLocators
import random
import string

@given('the user is in the Php_travel page')
def go_to_homepage(context):
    context.browser.get(EnvSetup.SITE)


@step('the user click on My Account in the homepage')
def click_my_account(context):
    context.browser.find_element(HomePageLocators.myAccount[0], HomePageLocators.myAccount[1]).click()


@step('the user click on Sign Up in My Account')
def click_signup(context):
    context.browser.find_element(HomePageLocators.signUp[0], HomePageLocators.signUp[1]).click()


@step('the user input first name as "{first_name}" in the sign up page')
def input_first_name(context, first_name):
    context.browser.find_element(SignUpLocators.firstname_Input[0], SignUpLocators.firstname_Input[1]).send_keys(
        first_name)

# from behave import given, when, then, use_step_matcher
# use_step_matcher("re")
@step('the user input last name as "{last_name}" in the sign up page')
def input_last_name(context, last_name):
    context.browser.find_element(SignUpLocators.lastname_Input[0], SignUpLocators.lastname_Input[1]).send_keys(
        last_name)


@step('the user input phone as "{phone}" in the sign up page')
def input_phone(context, phone):
    context.browser.find_element(SignUpLocators.phone_Input[0], SignUpLocators.phone_Input[1]).send_keys(
        phone)


@step('the user input email in the sign up page')
def input_email(context):
    randomdigits = CommonFunctionalities.Random_Digits(5)
    text = "HuyLe"
    gmail = "@gmail.com"
    context.browser.find_element(SignUpLocators.email_Input[0], SignUpLocators.email_Input[1]).send_keys(
        text + randomdigits + gmail)

@step('the user input password as "{password}" in the sign up page')
def input_password(context, password):
    context.browser.find_element(SignUpLocators.password_Input[0], SignUpLocators.password_Input[1]).send_keys(
        password)


@step('the user input confirm password as "{confirm_password}" in the sign up page')
def input_confirm_password(context, confirm_password):
    context.browser.find_element(SignUpLocators.confirmpassword_Input[0], SignUpLocators.confirmpassword_Input[1]).send_keys(confirm_password)

@when('the user click on Sign up button in the sign up page')
def click_signup_button(context):
    context.browser.find_element(SignUpLocators.signup_Button[0], SignUpLocators.signup_Button[1]).click()

@then('Verify first name as "{first_name}" and last name as "{last_name}" in my account page')
def verify_signup_successfully(context, first_name, last_name):
    actual_fullname = context.browser.find_element(MyAccountLocators.fullname_text[0],
                                                   MyAccountLocators.fullname_text[1]).text
    assert_that(actual_fullname, equal_to("Hi, " + first_name + " " + last_name), 'Verify sign up successfully')
