from Pages import HomePage_Elements, RegisterPage_Elements
from Common import CommonFunctions


class HomePage():
    def __init__(self, driver):
        self.driver = driver

    def Verify_Register_Successfully(self):
        pre_fix = 'huyle' + CommonFunctions.random_string(5)
        domain = '@gmail.com'
        container_Data = ('Huy', 'Le', pre_fix + domain, '01225888777', 'abc123', 'abc123')
        myAccountLink = self.driver.find_element(HomePage_Elements.myAccountLink_CSS_Path[0],
                                                 HomePage_Elements.myAccountLink_CSS_Path[1]).click()
        registerLink = self.driver.find_element(HomePage_Elements.registerLink_CSS_Path[0],
                                                HomePage_Elements.registerLink_CSS_Path[1]).click()
        firstNameField = self.driver.find_element(RegisterPage_Elements.firstNameField_CSS_Path[0],
                                                  RegisterPage_Elements.firstNameField_CSS_Path[1]).send_keys(
            container_Data[0])
        lastNameField = self.driver.find_element(RegisterPage_Elements.lastNameField_CSS_Path[0],
                                                 RegisterPage_Elements.lastNameField_CSS_Path[1]).send_keys(
            container_Data[1])
        emailField = self.driver.find_element(RegisterPage_Elements.emailField_CSS_Path[0],
                                              RegisterPage_Elements.emailField_CSS_Path[1]).send_keys(container_Data[2])
        telePhoneField = self.driver.find_element(RegisterPage_Elements.telePhoneField_CSS_Path[0],
                                                  RegisterPage_Elements.telePhoneField_CSS_Path[1]).send_keys(
            container_Data[3])
        passwordField = self.driver.find_element(RegisterPage_Elements.passwordField_CSS_Path[0],
                                                 RegisterPage_Elements.passwordField_CSS_Path[1]).send_keys(
            container_Data[4])
        confirmPasswordField = self.driver.find_element(RegisterPage_Elements.confirmPasswordField_CSS_Path[0],
                                                        RegisterPage_Elements.confirmPasswordField_CSS_Path[
                                                            1]).send_keys(
            container_Data[5])
        PolicyCb = self.driver.find_element(RegisterPage_Elements.PolicyCb_CSS_Path[0],
                                            RegisterPage_Elements.PolicyCb_CSS_Path[1]).click()
        continueButton = self.driver.find_element(RegisterPage_Elements.continueButton_CSS_Path[0],
                                                  RegisterPage_Elements.continueButton_CSS_Path[1]).click()
