from selenium import webdriver
from selenium.webdriver.common.by import By

# Locator of HomePage

sign_in = (By.CSS_SELECTOR, '.login')
product1 = (By.XPATH,'//*[@id="homefeatured"]/li[1]')

product1_add_btn = (By.XPATH,
                    '//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[1]/span')
product2 = (By.CSS_SELECTOR, 'img[title="Blouse"]')
product2_add_btn = (By.XPATH,
                    '//li[@class="ajax_block_product col-xs-12 col-sm-4 col-md-3 last-item-of-mobile-line hovered"]//span[contains(text(),"Add to cart")]')
# Locator of Authencation Page

create_email_field = (By.CSS_SELECTOR, 'input#email_create')
Email_field = (By.CSS_SELECTOR, 'input#email')
password_field = (By.CSS_SELECTOR, 'input#passwd')
caa_btn = (By.CSS_SELECTOR, 'button#SubmitLogin')
caa_btn = (By.CSS_SELECTOR, 'button#SubmitCreate')

# Locator of Create Account Page
gender_male = (By.CSS_SELECTOR, 'input#id_gender1')
genter_femaile = (By.CSS_SELECTOR, 'input#id_gender2')
firstname_field = (By.CSS_SELECTOR, 'input#customer_firstname')
lastname_filed = (By.CSS_SELECTOR, 'input#customer_lastname')
password_field = (By.CSS_SELECTOR, 'input#passwd')
date_dropdown = (By.CSS_SELECTOR, 'select#days')
month_dropdown = (By.CSS_SELECTOR, 'select#months')
year_dropdown = (By.CSS_SELECTOR, 'select#years')
cus_firstname_field = (By.CSS_SELECTOR, 'input#firstname')
cus_lastname_field = (By.CSS_SELECTOR, 'input#lastname')
cus_company_field = (By.CSS_SELECTOR, 'input#company')
cus_address1_field = (By.CSS_SELECTOR, 'input#address1')
cus_address2_field = (By.CSS_SELECTOR, 'input#address2')
cus_city_field = (By.CSS_SELECTOR, 'input#city')
cus_state_dropdown = (By.CSS_SELECTOR, 'select#id_state')
cus_postcode_field = (By.CSS_SELECTOR, 'input#postcode')
cus_country_Dropdown = (By.CSS_SELECTOR, 'select#id_country')
cus_additional_field = (By.CSS_SELECTOR, 'textarea#other')
cus_homephone = (By.CSS_SELECTOR, 'input#phone')
cus_mobiphone_field = (By.CSS_SELECTOR, 'input#phone_mobile')
cus_allias = (By.CSS_SELECTOR, 'input#alias')
register_btn = (By.CSS_SELECTOR, 'button#submitAccount')
