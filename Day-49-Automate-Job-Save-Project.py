from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = "/Development/chromedriver.exe"
USER_EMAIL = "saifulasus696@gmail.com"
PASSWORD = "Saiful2work"
ser = Service(chrome_driver_path)
opt = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=ser, options=opt)
driver.maximize_window()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3226584108&f_AL=true&geoId=102713980&keywords=data%20analyst&location=India&refresh=true")


driver.find_element(By.LINK_TEXT, "Sign in").click()

driver.find_element(By.NAME, "session_key").send_keys(USER_EMAIL)

driver.find_element(By.NAME, "session_password").send_keys(PASSWORD)

driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()


driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button').click()

job_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for job in job_listings:
    print(f"Saved: {job.text}")
    driver.execute_script("arguments[0].click();", job)
    time.sleep(2)

    save_button = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-save-button"))))