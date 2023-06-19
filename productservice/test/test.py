from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#register
driver.get('http://localhost:8888/EShop-1.0.0/')

driver.find_element(By.LINK_TEXT, "Noch nicht registriert?").click()

driver.find_element(By.NAME, "firstname").send_keys("test01")
driver.find_element(By.NAME, "lastname").send_keys("test02")
driver.find_element(By.NAME, "username").send_keys("test03")
driver.find_element(By.NAME, "password1").send_keys("1234")
driver.find_element(By.NAME, "password2").send_keys("1234")
driver.find_element(By.NAME, "method:execute").click()

#login
driver.get('http://localhost:8888/EShop-1.0.0/')

driver.find_element(By.NAME, "username").send_keys("test03")
driver.find_element(By.NAME, "password").send_keys("1234")
driver.find_element(By.NAME, "method:execute").click()

logout_button = driver.find_element(By.LINK_TEXT, "Logout")

assert logout_button is not None

#logout
logout_button.click()

#TBD assert we are logged out

#login as admin
#login
driver.get('http://localhost:8888/EShop-1.0.0/')

driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin")
driver.find_element(By.NAME, "method:execute").click()

#list all products
driver.find_element(By.LINK_TEXT, "Alle Produkte").click()

# TBD
#assert all products exist

#TBD
#create / update / list /delete product
#create / update / list /delete category
#search by name/price min. / price max.

driver.quit()
