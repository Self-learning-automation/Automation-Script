from selenium.webdriver.common.by import By

myAccountLink_CSS_Path = (By.CSS_SELECTOR, "a[title='My Account']")
registerLink_CSS_Path = (By.CSS_SELECTOR, "ul.dropdown-menu.dropdown-menu-right > li:nth-of-type(1) > a")
desktops_CSS_Path = (By.CSS_SELECTOR,'li.dropdown:nth-child(1)')
macInDesktops_CSS_Path = (By.CSS_SELECTOR, "a[href='https://demo.opencart.com/index.php?route=product/category&path=20_27']")
homepage_CSS_Path = (By.CSS_SELECTOR,"a[href='https://demo.opencart.com/index.php?route=common/home']")