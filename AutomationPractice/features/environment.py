from selenium import webdriver
from features.browsers.browser import Browser
from features.Pages.HomePage import HomePage
from features.Pages.AuthencationPage import Authencation
from features.Pages.CreateAccountPage import CreateAccount


def init_browser_session(context):
    context.browser = Browser().make_browser()
    return context


def before_scenario(context, scenario):
    context = init_browser_session(context)
    context.home_page = HomePage(context.browser)
    context.authencation_page = Authencation(context.browser)
    context.createaccount_page = CreateAccount(context.browser)


def after_scenario(context, scenario):
    context.browser.quit()
