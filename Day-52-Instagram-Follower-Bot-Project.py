from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = Service("/Development/chromedriver.exe")
SIMILAR_ACCOUNT = "python.hub"
INSTAGRAM_EMAIL = "bandotech46@gmail.com"
INSTAGRAM_PASSWORD = "Hiinstagram12"
LOGIN_URL = "https://www.instagram.com/accounts/login/"
BASE_URL = "https://www.instagram.com/"
driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)

class InstaFollowers:
    def __int__(self):
        self.driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get(LOGIN_URL)
        time.sleep(5)
        instagram_email = self.driver.find_element(By.NAME, "username")
        instagram_email.send_keys(INSTAGRAM_EMAIL)
        time.sleep(2)
        instagram_pass = self.driver.find_element(By.NAME, "password")
        instagram_pass.send_keys(INSTAGRAM_PASSWORD)
        instagram_pass.send_keys(Keys.ENTER)
        time.sleep(3)
        not_now = self.driver.find_element(By.CSS_SELECTOR, ".cmbtv button")
        not_now.click()
        time.sleep(2)
        noti_not_now = self.driver.find_element(By.CLASS_NAME, "_a9_1")
        noti_not_now.click()

    def find_followers(self):
        self.driver.get(f"{BASE_URL}{SIMILAR_ACCOUNT}")
        time.sleep(5)
        followers = self.driver.find_element(By.CSS_SELECTOR, "._aa_7 a")
        followers.click()
        time.sleep(2)
        # dialog = self.driver.find_element(By.CLASS_NAME, "i85zmo3j")
        # for i in range(3):
        #     self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', dialog)
        #     time.sleep(2)

    def follow(self):
        scrolling = True
        while scrolling:
            list_of_followers = self.driver.find_elements(By.CSS_SELECTOR, '._aano button')
            print(len(list_of_followers))
            if len(list_of_followers) != 0:
                for item in list_of_followers:
                    print(item.text)
                    if item.text == "Follow":
                        print("click")
                        item.click()
                        time.sleep(2)
            else:
                break

bot = InstaFollowers()
bot.login()
bot.find_followers()
bot.follow()