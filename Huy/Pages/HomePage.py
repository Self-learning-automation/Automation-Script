from Pages import HomePage_Elements, RegisterPage_Elements
from Common.CommonFunctions import Common

class HomePage():
    def __init__(self, driver):
        self.driver = driver

    def Verify_Register_Successfully(self):
        pre_fix = 'huyle' + Common.Random_string(5)
        domain = '@gmail.com'
        container_Data = ('Huy', 'Le', pre_fix + domain, '01225888777', 'abc123', 'abc123')
        self.driver.find_element(HomePage_Elements.myAccountLink_CSS_Path[0],
                                                 HomePage_Elements.myAccountLink_CSS_Path[1]).click()
        self.driver.find_element(HomePage_Elements.registerLink_CSS_Path[0],
                                                HomePage_Elements.registerLink_CSS_Path[1]).click()
        self.driver.find_element(RegisterPage_Elements.firstNameField_CSS_Path[0],
                                                  RegisterPage_Elements.firstNameField_CSS_Path[1]).send_keys(
            container_Data[0])
        self.driver.find_element(RegisterPage_Elements.lastNameField_CSS_Path[0],
                                                 RegisterPage_Elements.lastNameField_CSS_Path[1]).send_keys(
            container_Data[1])
        self.driver.find_element(RegisterPage_Elements.emailField_CSS_Path[0],
                                              RegisterPage_Elements.emailField_CSS_Path[1]).send_keys(container_Data[2])
        self.driver.find_element(RegisterPage_Elements.telePhoneField_CSS_Path[0],
                                                  RegisterPage_Elements.telePhoneField_CSS_Path[1]).send_keys(
            container_Data[3])
        self.driver.find_element(RegisterPage_Elements.passwordField_CSS_Path[0],
                                                 RegisterPage_Elements.passwordField_CSS_Path[1]).send_keys(
            container_Data[4])
        self.driver.find_element(RegisterPage_Elements.confirmPasswordField_CSS_Path[0],
                                                        RegisterPage_Elements.confirmPasswordField_CSS_Path[
                                                            1]).send_keys(
            container_Data[5])
        self.driver.find_element(RegisterPage_Elements.PolicyCb_CSS_Path[0],
                                            RegisterPage_Elements.PolicyCb_CSS_Path[1]).click()
        self.driver.find_element(RegisterPage_Elements.continueButton_CSS_Path[0],
                                                  RegisterPage_Elements.continueButton_CSS_Path[1]).click()


    def ClickMacmenuFromDesktops(self):
        self.driver.find_element(HomePage_Elements.homepage_CSS_Path[0],HomePage_Elements.homepage_CSS_Path[1]).click()
        macInDesktops = self.driver.find_element(HomePage_Elements.desktops_CSS_Path[0],
                                                 HomePage_Elements.desktops_CSS_Path[1])
        macSubLink = self.driver.find_element(HomePage_Elements.macInDesktops_CSS_Path[0],
                                              HomePage_Elements.macInDesktops_CSS_Path[1])
        common = Common(self.driver)
        common.HoverandClick(macInDesktops, macSubLink)
