import time

from behave import *
from selenium.webdriver.common.by import By
from Config.env_setup import EnvSetup
from hamcrest import assert_that, equal_to
from utilities.Random import Random
rd = Random()


@given('the user is in the Automationpractice homepage')
def go_to_homepage(context):
    context.browser.get(EnvSetup.SITE)


@when('the user click on Sign in')
def click_sign_in(context):
    context.home_page.click_signin()


@when('user enter Email address')
def enter_email_adress(context):
    context.authencation_page.enter_createemail_field("Tuanbui"+str(int(round(time.time())))+"@gmail.com")


# Tuanbui"+str(int(round(time.time())))+"@gmail.com

@when('User click on "Create Account"')
def click_create_account(context):
    context.authencation_page.click_create_button()


@when('User fill all personal information in the form')
def enter_full_information(context):
    context.createaccount_page.create_account_flow(rd.randomString(8), rd.randomString(8), rd.randomString(8),
                                                   rd.randomString(5), rd.randomString(6), rd.randomString(6),
                                                   rd.randomString(6), rd.randomString(6), rd.randomString(6),
                                                   rd.randomNumber1(5, "0123456789"), rd.randomString(6),
                                                   rd.randomNumber1(10, "0123456789"), rd.randomString(6))


@then('Verify User register successfully')
def verify_register_user(context):

    context.createaccount_page.verify_register_successfully()
