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
