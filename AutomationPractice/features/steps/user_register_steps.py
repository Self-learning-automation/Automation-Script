from behave import *
from selenium.webdriver.common.by import By
from Config.env_setup import EnvSetup
from hamcrest import assert_that, equal_to
from ultilities.Random import Random
rd = Random()


@given('the user is in the Automationpractice homepage')
def go_toHomepage(context):
    context.browser.get(EnvSetup.SITE)


@when('the user click on Sign in')
def click_Signin(context):
    context.home_page.clickSignin()


@when('user enter Email address "{email_address}"')
def enter_EmailAdress(context, email_address):
    context.authencation_page.enterCreateEmailField(email_address)


# Tuanbui"+str(int(round(time.time())))+"@gmail.com

@when('User click on "Create Account"')
def click_CreateAccount(context):
    context.authencation_page.clickCreateButton()


@when('User fill all personal information in the form')
def enter_fullinformation(context):
    context.createaccount_page.CreateAccountFlow(rd.randomString(8), rd.randomString(8), rd.randomString(8),
                                                 rd.randomString(5), rd.randomString(6), rd.randomString(6),
                                                 rd.randomString(6), rd.randomString(6),
                                                 rd.randomString(6), rd.randomNumber1(5, "0123456789"),
                                                 rd.randomString(6), rd.randomNumber1(10, "0123456789"),
                                                 rd.randomString(6))


@then('Verify User register successfully')
def verify_impl(context):
    expected_result = "Welcome to your account. Here you can manage all of your personal information and orders."
    actual_result = context.browser.find_element(By.CSS_SELECTOR, 'p.info-account').text
    assert_that(actual_result, equal_to(expected_result), 'Verify Message')
