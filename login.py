# Created by Patalin.py
# Follow @Patalin.py on Instagram for more small projects like this

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrorme_driver_path = Service('/Users/macbookpro/Desktop/chromedriver')
driver = webdriver.Chrome(service=chrorme_driver_path)
driver.get('https://www.saucedemo.com/')

# Find elements username and password
username = driver.find_element(By.NAME, 'user-name')
password = driver.find_element(By.NAME, 'password')

# Input data inside username and password
username.send_keys('standard_user')
password.send_keys('secret_sauce')

# Press ENTER to login
username.send_keys(Keys.ENTER)

# driver.quit()