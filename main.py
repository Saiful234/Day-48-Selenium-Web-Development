from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time
USERNAME = "bandotech96@gmail.com"
PASSWORD = "Hieveryone12"
chrome_driver_path = "/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/")
driver.maximize_window()
time.sleep(10)
decline_button = driver.find_element(By.XPATH, '//*[@id="c-1560500889"]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]')
decline_button.click()
login = driver.find_element(By.LINK_TEXT, "Log in")

login.click()

try:
    time.sleep(10)
    more_option = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div[1]/div/div/div[3]/span/button')
    more_option.click()
    print("more option")
except NoSuchElementException:
    time.sleep(5)
    login_fb = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
    login_fb.click()
    print("logged in fb")
finally:
    time.sleep(5)
    login_fb = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
    login_fb.click()
    print("logged more options")

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)
print(driver.title)

fb_username = driver.find_element(By.NAME, "email")
fb_username.send_keys(USERNAME)
fb_password = driver.find_element(By.NAME, "pass")
fb_password.send_keys(PASSWORD)
fb_login_button = driver.find_element(By.NAME, "login")
fb_login_button.click()
driver.switch_to.window(base_window)
print(driver.title)
location_allow = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div/div/div[3]/button[1]')
location_allow.click()
# driver.close()