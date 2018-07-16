from selenium.webdriver.common.by import By

addtocart_CSS_Path = (By.CSS_SELECTOR, '.button-group>button>span')
shoppingcartButton_CSS_Path = (By.CSS_SELECTOR, '#cart>button')
checkoutLink_CSS_Path = (By.CSS_SELECTOR, "a[href='https://demo.opencart.com/index.php?route=checkout/checkout']:nth-child(2)")
checkoutButton_CSS_Path = (By.CSS_SELECTOR, ".pull-right>a")
alert_NotAvailableMessage = (By.CSS_SELECTOR, '.alert.alert-danger')
actual_SuccessfullyMessage = (By.CSS_SELECTOR,'.alert.alert-success')
expected_Product_Name = (By.CSS_SELECTOR,'.alert.alert-success>a:nth-child(2)')
expected_Page_Name = (By.CSS_SELECTOR,'.alert.alert-success>a:nth-child(3)')






