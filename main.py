# Created by Patalin.py
# Follow @Patalin.py on Instagram for more small projects like this

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrorme_driver_path = Service('/Users/macbookpro/Desktop/chromedriver')
driver = webdriver.Chrome(service=chrorme_driver_path)
driver.get('https://www.python.org/')

events_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
events_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

events = {}

for n in range(len(events_times)):
    events[n] = {
        'time': events_times[n].text,
        'name': events_names[n].text,
    }

print(events)

driver.quit()



