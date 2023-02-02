from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Set up executable path for chromedriver:
service = Service(executable_path="Users/aki/chromedriver")

# Create Options object in order to add custom option that will prevent Selenium from automatically closing browser:
options = Options()
options.add_experimental_option("detach", True)

# Webdriver setup:
driver = webdriver.Chrome(service=service, options=options)


# -------------------------- MOCK-UP FORM SUBMISSION --------------------------
driver.get(
    "https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")

# Get element tags by tag names/ CSS selector:
first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
button = driver.find_element(By.CSS_SELECTOR, "form button")

# Type strings into input:
first_name.send_keys("Alexandros")
last_name.send_keys("Charangionis")
email.send_keys("alexandroscharangionis@gmail.com")

# Submit form
button.click()


# -------------------------- AUTOMATED COOKIE CLICKER --------------------------

driver.get("https://orteil.dashnet.org/cookieclicker/")

# Find website cookie disclaimer and click it:
got_it = driver.find_element(By.LINK_TEXT, "Got it!")
got_it.click()

# Find 'english' language button and click it:
english_lang = driver.find_element(By.ID, "langSelect-EN")
english_lang.click()

# Find cookie button and click it continuously:
cookie_button = driver.find_element(By.ID, "bigCookie")
while True:
    cookie_button.click()
