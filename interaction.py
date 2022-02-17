from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrorme_driver_path = Service('/Users/macbookpro/Desktop/chromedriver')
driver = webdriver.Chrome(service=chrorme_driver_path)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

no_of_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')

print(no_of_articles.text)

driver.quit()