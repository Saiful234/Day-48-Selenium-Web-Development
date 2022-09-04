from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


PROMISED_DOWN = 2
PROMISED_UP = 1

CHROME_DRIVER_PATH = Service("/Development/chromedriver.exe")

TWITTER_EMAIL = "bandotech46@gmail.com"
TWITTER_PASSWORD = "Hitwitter12"


class InternetSpeedTwitterBot:
    def __int__(self, driver_path):
        self.driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)
        self.down_speed = 0
        self.up_speed = 0

    def get_internet_speed(self):
        self.driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)
        self.driver.get("https://www.speedtest.net/")
        close_button = self.driver.find_element(By.CSS_SELECTOR, "#onetrust-close-btn-container button")
        close_button.click()
        go_button = self.driver.find_element(By.XPATH,
                                        '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(60)
        self.down_speed = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        print(f"Your internet download speed is {self.down_speed}Mbps")
        self.up_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(f"Your internet upload speed is {self.up_speed}Mbps")
        self.driver.close()

    def tweet_at_provider(self):
        self.driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(16)
        email = self.driver.find_element(By.NAME, "text")
        email.send_keys(TWITTER_EMAIL)
        time.sleep(5)
        next_button = self.driver.find_element(By.XPATH,
                                          '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()
        time.sleep(5)
        verify_button = self.driver.find_element(By.NAME, "text")
        verify_button.send_keys("Bandotech46O")
        verify_button.send_keys(Keys.ENTER)
        time.sleep(2)
        twitter_password = self.driver.find_element(By.NAME, "password")
        twitter_password.send_keys(TWITTER_PASSWORD)
        twitter_password.send_keys(Keys.ENTER)
        global PROMISED_DOWN, PROMISED_UP
        if int(self.down_speed) < PROMISED_DOWN and int(self.up_speed) < PROMISED_UP:
            tweet_text = f"Hey Internet service provider, why is my internet speed {self.down_speed}/{self.up_speed} when I pay for 4down/1up Mbps"

            enter_tweet = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'div[data-testid="tweetTextarea_0"][role = "textbox"]')))
            enter_tweet.send_keys(tweet_text)
            tweet_button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]')
            tweet_button.click()
        else:
            self.driver.close()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()


