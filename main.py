from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# price = driver.find_element(By.ID, "productTitle")
# print(price.text)

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.get_attribute("href"))

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")

event_text = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_text[n].text,
    }

print(events)


driver.close()