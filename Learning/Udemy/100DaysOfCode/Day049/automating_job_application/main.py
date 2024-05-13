import os
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = r"Day048/Resources/ChromeDriver/chromedriver.exe"
LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3632384082&f_AL=true&geoId=105790653&keywords=c%2B" \
               "%2B%20&location=Hanoi%2C%20Hanoi%2C%20Vietnam&refresh=true"
ACCOUNT_EMAIL = "thanhtungpfievpro@gmail.com"
ACCOUNT_PASSWORD = os.getenv('ACCOUNT_PASSWORD')

# Create an Options class, necessary to keep open the Chrome Browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path=CHROME_DRIVER_PATH)

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(LINKEDIN_URL)
driver.maximize_window()

signin_button = driver.find_element(By.CSS_SELECTOR,
                                    "body > div.base-serp-page > header > nav > div > "
                                    "a.nav__button-secondary.btn-md.btn-secondary-emphasis")

signin_button.click()

# Wait for the next page to load.
time.sleep(5)

username_field = driver.find_element(By.ID, "username")
username_field.send_keys(ACCOUNT_EMAIL)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# minimize the pop-up chat window so the save button can be clicked

chat_min = driver.find_element(By.CSS_SELECTOR, "#ember114")
chat_min.click()

# Save all the jobs and follow all the companies
job_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
listing_no = len(job_listings)
print(listing_no)

# Save the job
for index in range(listing_no):
    job_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
    job = job_listings[index]
    job.click()
    time.sleep(1)
    save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_button.click()

    # check to see if company has a page and follow if they do
    try:
        company = driver.find_element(By.CLASS_NAME, "jobs-details-top-card__company-url")
        company.click()
        time.sleep(5)
        follow_button = driver.find_element(By.CLASS_NAME, "follow")
        follow_button.click()
        driver.back()
    except NoSuchElementException:
        pass

# driver.close()
# driver.quit()
