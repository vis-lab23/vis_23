from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#cregister
driver.get('http://localhost:8888/EShop-1.0.0/')

register_link = driver.find_element(By.LINK_TEXT, "Noch nicht registriert?")
register_link.click()

name_field = driver.find_element(By.NAME, "firstname").send_keys("test01")
lastname_field = driver.find_element(By.NAME, "lastname").send_keys("test02")
username_field = driver.find_element(By.NAME, "username").send_keys("test03")
password_field = driver.find_element(By.NAME, "password1").send_keys("1234")
password2_field = driver.find_element(By.NAME, "password2").send_keys("1234")
register_button = driver.find_element(By.NAME, "method:execute")
register_button.click()

#login
driver.get('http://localhost:8888/EShop-1.0.0/')

username_field = driver.find_element(By.NAME, "username").send_keys("test03")
password_field = driver.find_element(By.NAME, "password").send_keys("1234")
login_button = driver.find_element(By.NAME, "method:execute")
login_button.click()

#logout
logout_link = driver.find_element(By.LINK_TEXT, "Logout")
logout_link.click()
#TBD assert we are logged out

#login as admin
#login
driver.get('http://localhost:8888/EShop-1.0.0/')

username_field = driver.find_element(By.NAME, "username").send_keys("admin")
password_field = driver.find_element(By.NAME, "password").send_keys("admin")
login_button = driver.find_element(By.NAME, "method:execute")
login_button.click()

#list all products
list_link = driver.find_element(By.LINK_TEXT, "Alle Produkte")
list_link.click()

# TBD
#assert all products exist

#TBD
#create / update / list /delete product
#create / update / list /delete category
#search by name/price min. / price max.

driver.quit()
