import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='E:\Python selenium\pythonseleniumproject1\driver\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://test-talent.talent-troop.com/auth/login")
driver.maximize_window()
web_title = driver.title
print(web_title)
time.sleep(1)

# Locate the Signin form fields and fill them
email_signin_field = driver.find_element("xpath", "//input[@id='mat-input-0']")
email_signin_field.clear()
email_signin_field.send_keys("taronej783@byorby.com")
time.sleep(1)
password_signin_field = driver.find_element("xpath", "//input[@id='mat-input-1']")
password_signin_field.clear()
password_signin_field.send_keys("123456")
time.sleep(1)

# Remember Me (optional)
remember_me_checkbox = driver.find_element("xpath", "//span[@class='mat-checkbox-inner-container']")
remember_me_checkbox.click()
time.sleep(2)

# Click on the "Sign in" button
signin_button = driver.find_element("xpath", "//span[normalize-space()='SIGN IN']")
signin_button.click()
time.sleep(2)

# Locate the job button and click on it
# job_button = driver.find_element("xpath", "//mat-card-title[@class='mat-card-title mat-tooltip-trigger']")
# job_button.click()
# time.sleep(2)

# #locate and click the "Applied" button
# applied_button = driver.find_element("xpath", "(//span[normalize-space()='Applied'])[1]")
# applied_button.click()
# time.sleep(2)
#
# # Locate the back button and click on it
# back_button = driver.find_element("xpath", "//span[normalize-space()='Back']")
# back_button.click()
# time.sleep(2)
# Click on the "My profile" button
profile_button = driver.find_element("xpath", "//span[contains(text(),'My Profile')]")
profile_button.click()
time.sleep(2)
# Click on the "My profile" edit button
profile_pic_button = driver.find_element("xpath", "//mat-icon[@mattooltip='Change your image']")
profile_pic_button.click()
time.sleep(2)
# Click on the "My profile" edit button
# profile_pic = driver.find_element("xpath", "//mat-icon[@mattooltip='Change your image']")
# profile_pic.send_keys("E:\dummy img.png")
# time.sleep(2)
objective_field = driver.find_element("xpath", "//textarea[@id='mat-input-3']")
objective_field.clear()
objective_field.send_keys("ABCD")
time.sleep(2)
cancelButton = driver.find_element("xpath", "//span[normalize-space()='Cancel']").click()
time.sleep(3)
edit_field = driver.find_element("xpath", "//mat-icon[@mattooltip='edit']")
edit_field.click()
time.sleep(2)
# Fill in Talent Basic Information fields
first_name_field = driver.find_element("xpath", "//input[@id='mat-input-4']")
first_name_field.clear()
first_name_field.send_keys("taraaa")
time.sleep(2)
last_name_field = driver.find_element("xpath", "//input[@id='mat-input-5']")
last_name_field.clear()
last_name_field.send_keys("oneee")
time.sleep(2)
mobile_number_field = driver.find_element("xpath", "//input[@id='mat-input-7']")
mobile_number_field.clear()
mobile_number_field.send_keys("01712111111")
time.sleep(2)
father_name_field = driver.find_element("xpath", "//input[@id='mat-input-8']")
father_name_field.clear()
father_name_field.send_keys("Jowen")
time.sleep(2)
mother_name_field = driver.find_element("xpath", "//input[@id='mat-input-9']")
mother_name_field.clear()
mother_name_field.send_keys("Romger")
time.sleep(2)
dob_field = driver.find_element("xpath", "//*[@id='talent-basic']/div/div[3]/mat-form-field[1]/div/div[1]/div[4]/mat-datepicker-toggle/button")
dob_field.click()
time.sleep(2)

do_field = driver.find_element("xpath", "//*[@id='mat-datepicker-0']/mat-calendar-header/div/div/button[1]")
do_field.click()
time.sleep(3)

d_field = driver.find_element("xpath", "//div[normalize-space()='1998']")
d_field.click()
time.sleep(3)
month_ele = driver.find_element("xpath", "//div[normalize-space()='JAN']")
month_ele.click()
time.sleep(3)
day_ele = driver.find_element("xpath", "//div[normalize-space()='1']")
day_ele.click()

time.sleep(10)

# id_number_field.clear()
# id_number_field.send_keys("1234567890")
# time.sleep(2)
# # For Permanent Address
# time.sleep(0.5)
# permanent_country = driver.find_element("xpath", "//div[@id='mat-select-value-3']")
# permanent_country.click()
# countries_list = driver.find_elements("xpath", "//span[@class='mat-option-text'][normalize-space()='Bangladesh']")
# print("Available Permanent Country list: ", len(countries_list))
# time.sleep(0.2)
# for country in countries_list:
#     if country.text == "Argentina":
#         print("Name:", country.text)
#         country.click()
#         break
# Select Country from the dropdown
# country_dropdown = driver.find_element("xpath", "//div[@id='mat-select-value-1']")
# country_dropdown.click()
# time.sleep(5)
#country_dropdown.select_by_visible_text("Bangladesh")

# Select City/State/Province from the dropdown
# city_state_dropdown = driver.find_element("xpath", "//div[@id='mat-select-value-2']")
# city_state_dropdown.click()
# time.sleep(5)
#city_state_dropdown.select_by_visible_text("Dhaka")

# Check the "Is Present address same as permanent address?" checkbox
is_present_address_checkbox = driver.find_element("xpath", "//span[@class='mat-checkbox-inner-container']")
is_present_address_checkbox.click()
time.sleep(5)
# # Select Blood Group from the dropdown
# blood_group_dropdown = Select(driver.find_element("xpath", "//select[@id='blood_group']"))
# blood_group_dropdown.select_by_visible_text("O+")
#
# # Select Gender from the dropdown
# gender_dropdown = Select(driver.find_element("xpath", "//select[@id='gender']"))
# gender_dropdown.select_by_visible_text("Male")
#
# # Select Nationality from the dropdown
# nationality_dropdown = Select(driver.find_element("xpath", "//select[@id='nationality']"))
# nationality_dropdown.select_by_visible_text("Bangladesh")
#
# # Click the "Submit" button
# submit_button = driver.find_element("xpath", "//button[normalize-space()='Submit']")
# submit_button.click()

# # Locate the "Create account" button and click on it
# create_account_button = driver.find_element("xpath","//span[normalize-space()='Create Account']")
# create_account_button.click()
# time.sleep(1)
# # Input data into registration form fields
# country_dropdown = driver.find_element("xpath", "//div[@id='mat-select-value-1']")
# country_dropdown.click()
# time.sleep(1)
# country_select = driver.find_element("xpath", "//span[normalize-space()='Bangladesh']")
# country_select.click()
# time.sleep(1)
# first_name_field = driver.find_element("xpath", "//input[@id='mat-input-2']")
# first_name_field.send_keys("geni")
# time.sleep(1)
# last_name_field = driver.find_element("xpath", "//input[@id='mat-input-3']")
# last_name_field.send_keys("faar")
# time.sleep(1)
# password_field = driver.find_element("xpath", "//input[@id='mat-input-4']")
# password_field.send_keys("123456")
# time.sleep(1)
# confirm_password_field = driver.find_element("xpath","//input[@id='mat-input-5']")
# confirm_password_field.send_keys("123456")
# time.sleep(1)
# #mobile_prefix_code_field = driver.find_element("xpath", "//input[@id='mat-input-6']")
# #mobile_prefix_code_field.send_keys("+1")
# time.sleep(1)
# mobile_number_field = driver.find_element("xpath", "//input[@id='mat-input-7']")
# mobile_number_field.send_keys("01822222220")
# time.sleep(1)
# email_field = driver.find_element("xpath", "//input[@id='mat-input-8']")
# email_field.send_keys("genef52534@eimatro.com")
# time.sleep(1)
# send_otp_button = driver.find_element("xpath", "//span[normalize-space()='Send OTP to Email']")
# send_otp_button.click()
# time.sleep(15)
# otp_field = driver.find_element("xpath", "//input[@id='mat-input-7']")
# otp_field.send_keys("Cr3tcV")
# time.sleep(5)
# # Click on the "Create Account" button
# create_account_button = driver.find_element("xpath", "//input[@id='mat-input-11']")
# create_account_button.click()
# time.sleep(5)
#Close the browser
#driver.close()


