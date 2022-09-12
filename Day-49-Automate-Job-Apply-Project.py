from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

USER_EMAIL = "saifulasus696@gmail.com"
PASSWORD = "Saiful2work"
PHONE = "+919489151902"
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3226584108&f_AL=true&geoId=102713980&keywords=data%20analyst&location=India&refresh=true")


driver.find_element(By.LINK_TEXT, "Sign in").click()

driver.find_element(By.NAME, "session_key").send_keys(USER_EMAIL)

driver.find_element(By.NAME, "session_password").send_keys(PASSWORD)

driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()


driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button').click()

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for list in all_listings:
    print("called")
    list.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
        apply_button.click()

        # if phone field is empty, then fill phone number.
        phone = driver.find_element(By.CSS_SELECTOR, ".fb-single-line-text input")
        if phone.text == "":
            phone.send_keys(PHONE)


        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

    #     if the submit_button is a "Next" Button, then this is a multi-step application.
    if submit_button.get_attribute("data-control-name") == "continue_unify":
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal")
    except NoSuchElementException:
        print("no application button, skipped.")
        continue
