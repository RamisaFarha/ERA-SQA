import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#service = Service(executable_path='E:\Python selenium\pythonseleniumproject1\driver\msedgedriver.exe')
#driver = webdriver.Edge(service=service)
service = Service(executable_path='E:\Python selenium\pythonseleniumproject1\driver\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# Locate the "Register" button and click on it
register_button = driver.find_element("xpath","//a[normalize-space()='Register']")
register_button.click()
web_title=driver.title
print(web_title)
time.sleep(1)

# Input Your Personal Details data into registration form fields
gender_field_male = driver.find_element("xpath","//input[@id='gender-male']")
gender_field_male.click()
time.sleep(1)
gender_field_female = driver.find_element("xpath","//input[@id='gender-female']")
gender_field_female.click()
time.sleep(1)
first_name_field = driver.find_element("xpath", "//input[@id='FirstName']")
first_name_field.send_keys("Rami")
time.sleep(1)
last_name_field = driver.find_element("xpath", "//input[@id='LastName']")
last_name_field.send_keys("Fara")
time.sleep(1)
date_of_birth_field_day = driver.find_element("xpath", "//select[@name='DateOfBirthDay']")
date_of_birth_field_day.send_keys("7")
date_of_birth_field_month = driver.find_element("xpath","//select[@name='DateOfBirthMonth']")
date_of_birth_field_month.send_keys("May")
date_of_birth_field_year = driver.find_element("xpath","//select[@name='DateOfBirthYear']")
date_of_birth_field_year.send_keys("1990")
time.sleep(1)
email_field = driver.find_element("xpath", "//input[@id='Email']")
email_field.send_keys("rf@gmail.com")
time.sleep(1)

# Input data into Company Details
company_name_field = driver.find_element("xpath", "//input[@id='Company']")
company_name_field.send_keys("RF Inc")
time.sleep(1)

# Input the password and confirm password
password_field = driver.find_element("xpath", "//input[@id='Password']")
password_field.send_keys("123456")
time.sleep(1)
confirm_password_field = driver.find_element("xpath", "//input[@id='ConfirmPassword']")
confirm_password_field.send_keys("123456")
time.sleep(1)

# Click on the "Register" button
register_button = driver.find_element("xpath", "//button[@id='register-button']")
register_button.click()
time.sleep(1)

# Locate the "login" button and click on it
login_button = driver.find_element("xpath", "//a[normalize-space()='Log in']")
login_button.click()

# Close the browser
#driver.close()


