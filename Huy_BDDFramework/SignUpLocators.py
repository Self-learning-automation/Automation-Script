from selenium.webdriver.common.by import By


class SignUpLocators():
    signUpTitle = (By.CSS_SELECTOR, "title")
    firstname_Input = (By.CSS_SELECTOR, "[name='firstname']")
    lastname_Input = (By.CSS_SELECTOR, "[name='lastname']")
    phone_Input = (By.CSS_SELECTOR, "[name='phone']")
    email_Input = (By.CSS_SELECTOR, "[name='email']")
    password_Input = (By.CSS_SELECTOR, "[name='password']")
    confirmpassword_Input = (By.CSS_SELECTOR, "[name='confirmpassword']")
    signup_Button = (By.XPATH, "//button[contains(text(),' Sign Up')]")



