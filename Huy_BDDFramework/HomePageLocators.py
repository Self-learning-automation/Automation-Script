from selenium.webdriver.common.by import By


class HomePageLocators():
    myAccount = (By.XPATH, "//*[@id='collapse']//*[@id='li_myaccount']/a[contains(text(),' My Account ')]")
    signUp = (By.XPATH, "//*[@class ='open']//*[(contains(text(), '  Sign Up'))]")
    homepageTitle = (By.CSS_SELECTOR, "title")

