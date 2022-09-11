from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time
USERNAME = "bandotech46@gmail.com"
PASSWORD = "Hieveryone12"
chrome_driver_path = "/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
driver.get("https://tinder.com/")
# Cookies notification decline
time.sleep(10)
decline_button = driver.find_element(By.XPATH, '//*[@id="o-98920890"]/div/div[2]/div/div/div[1]/div[2]/button')
decline_button.click()
login = driver.find_element(By.LINK_TEXT, "Log in")

login.click()
# Try different login process
try:
    time.sleep(5)
    login_fb = driver.find_element(By.XPATH, '//*[@id="o-1827301966"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
    login_fb.click()
    print("logged in fb")

except NoSuchElementException:
    try:
        time.sleep(5)
        more_option = driver.find_element(By.XPATH,
                                          '//*[@id="o-1827301966"]/main/div/div[1]/div/div/div[3]/span/button')
        more_option.click()
        print("more option")
    except NoSuchElementException:
        print("Failed")
    else:
        time.sleep(5)
        login_fb = driver.find_element(By.XPATH,
                                       '//*[@id="o-1827301966"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
        login_fb.click()
        print("logged more options")

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
# Facebook login credentials
driver.switch_to.window(fb_login_window)
print(driver.title)
time.sleep(3)
fb_username = driver.find_element(By.NAME, "email")
fb_username.send_keys(USERNAME)
fb_password = driver.find_element(By.NAME, "pass")
fb_password.send_keys(PASSWORD)
fb_password.send_keys(Keys.ENTER)
# Tinder window location, notification and remind me later
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(9)
location_allow = driver.find_element(By.XPATH, '//*[@id="o-1827301966"]/main/div/div/div/div[3]/button[1]')

location_allow.click()

time.sleep(2)
decline_noti = driver.find_element(By.XPATH, '//*[@id="o-1827301966"]/main/div/div/div/div[3]/button[2]')
decline_noti.click()
time.sleep(7)
may_be_later = driver.find_element(By.XPATH, '//*[@id="o-1827301966"]/main/div/div/div[3]/button[2]')
may_be_later.click()
time.sleep(10)
for i in range(100):
    try:
        nope = driver.find_element(By.XPATH, '//*[@id="o-98920890"]/div/div[1]/div/div/main/div/div/div[1]/div/div[5]/div/div[2]/button')
        nope.click()
        time.sleep(2)
    except ElementClickInterceptedException:
        driver.find_element(By.CSS_SELECTOR, ".itsAMatch a").click()
    except NoSuchElementException:
        time.sleep(2)

driver.close()

