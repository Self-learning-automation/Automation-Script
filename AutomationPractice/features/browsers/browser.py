from selenium.webdriver.chrome.options import Options
from selenium import webdriver

class Browser:
    def make_browser(self):
        chrome_options = Options()
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_experimental_option("detach",True)
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver
