# To run this selenium test
# 1. pip install selenium
# 2. python3 test.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

base_url = "http://192.168.59.107:30115"

driver = webdriver.Chrome()

# Register
driver.get(base_url + '/EShop-1.0.0/')

driver.find_element(By.LINK_TEXT, "Noch nicht registriert?").click()

assert driver.find_element(By.TAG_NAME, "h2").text == "Registrierung"

driver.find_element(By.NAME, "firstname").send_keys("test01")
driver.find_element(By.NAME, "lastname").send_keys("test02")
driver.find_element(By.NAME, "username").send_keys("test03")
driver.find_element(By.NAME, "password1").send_keys("1234")
driver.find_element(By.NAME, "password2").send_keys("1234")
driver.find_element(By.NAME, "method:execute").click()

check = False
for element in driver.find_elements(By.TAG_NAME, "font"):
    if element.text == "user registered, please login":
        check = True
        break

for element in driver.find_elements(By.TAG_NAME, "span"):
    if element.text == "Benutzername bereits in Verwendung.":
        check = True
        break

assert check is True

# Login unprivileged user
driver.get(base_url + '/EShop-1.0.0/')

driver.find_element(By.NAME, "username").send_keys("test03")
driver.find_element(By.NAME, "password").send_keys("1234")
driver.find_element(By.NAME, "method:execute").click()

check = False
for row in driver.find_elements(By.CLASS_NAME, "row"):
    if row.text == "Sie sind eingeloggt als test01 test02":
        check = True
        break
assert check is True

# Logout
driver.find_element(By.LINK_TEXT, "Logout").click()

assert driver.find_element(By.TAG_NAME, "h2").text == "Login"

# Login as admin
driver.get(base_url + '/EShop-1.0.0/')

driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin")
driver.find_element(By.ID, "LoginAction__execute").click()

check = False
for row in driver.find_elements(By.CLASS_NAME, "row"):
    if row.text == "Sie sind eingeloggt als admin admin":
        check = True
        break
assert check is True

# Add Category
driver.find_element(By.LINK_TEXT, "Kategorien bearbeiten").click()
driver.find_element(By.NAME, "newCatName").send_keys("42")
driver.find_element(By.ID, "AddCategoryAction_category_submit").click()

driver.implicitly_wait(10)

check = False
for row in driver.find_elements(By.TAG_NAME, "tr"):
    if row.find_elements(By.TAG_NAME, "td")[1].text == "42":
        check = True
        break
assert check is True

# Add Product
driver.find_element(By.LINK_TEXT, "Produkt hinzufügen").click()
driver.find_element(By.NAME, "name").send_keys("Per Anhalter durch die Galaxis")
driver.find_element(By.NAME, "price").send_keys("42.42")

select = Select(driver.find_element(By.NAME, "categoryId"))
select.select_by_visible_text("42")

driver.find_element(By.NAME, "details").send_keys("Buch mit 42 Seiten")
driver.find_element(By.ID, "AddProductAction_product_submit").click()

driver.implicitly_wait(15)

check = False
for row in driver.find_elements(By.TAG_NAME, "tr"):
    columns = row.find_elements(By.TAG_NAME, "td")
    if columns[1].text == "Per Anhalter durch die Galaxis" and columns[3].text == "42":
        check = True
        break
assert check is True

# Search
driver.find_element(By.LINK_TEXT, "Alle Produkte").click()
driver.find_element(By.NAME, "searchValue").send_keys("Galaxis")
driver.find_element(By.ID, "SearchAction_search_submit").click()

check = False
for row in driver.find_elements(By.TAG_NAME, "tr"):
    columns = row.find_elements(By.TAG_NAME, "td")
    if columns[1].text == "Per Anhalter durch die Galaxis" and columns[3].text == "42":
        check = True
        break
assert check is True

# Delete Product
driver.find_element(By.LINK_TEXT, "Alle Produkte").click()

delete_product_button = None
for row in driver.find_elements(By.TAG_NAME, "tr"):
    columns = row.find_elements(By.TAG_NAME, "td")
    if columns[1].text == "Per Anhalter durch die Galaxis":
        delete_product_button = columns[5].find_element(By.TAG_NAME, "a")
        break

delete_product_button.click()

check = False
for row in driver.find_elements(By.TAG_NAME, "tr"):
    if row.find_elements(By.TAG_NAME, "td")[1].text == "Per Anhalter durch die Galaxis":
        check = True
        break

assert check is False

# Delete Category
driver.find_element(By.LINK_TEXT, "Kategorien bearbeiten").click()

delete_category_button = None
for row in driver.find_elements(By.TAG_NAME, "tr"):
    columns = row.find_elements(By.TAG_NAME, "td")
    if columns[1].text == "42":
        delete_category_button = columns[2].find_element(By.TAG_NAME, "a")
        break

delete_category_button.click()

check = False
for row in driver.find_elements(By.TAG_NAME, "tr"):
    if row.find_elements(By.TAG_NAME, "td")[1].text == "42":
        check = True
        break

assert check is False

# Logout
driver.find_element(By.LINK_TEXT, "Logout").click()

assert driver.find_element(By.TAG_NAME, "h2").text == "Login"

# Stop Selenium test
driver.quit()
