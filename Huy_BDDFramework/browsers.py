from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Browser:

    @staticmethod
    def make_browser():
        chrome_options = Options()
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument("--start-maximized")
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.implicitly_wait(10)
        return browser
