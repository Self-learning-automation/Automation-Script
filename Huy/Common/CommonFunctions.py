import  random
import string
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Pages import HomePage_Elements
class Common():
    def __init__(self, driver):
        self.driver = driver
    def Random_string(length):
        return ''.join(random.choice(string.ascii_letters) for m in range(length))
    def HoverandClick(self,menu, submenu):
        actions = ActionChains(self.driver)
        actions.move_to_element(menu)
        actions.click(submenu).perform()








