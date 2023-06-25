from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = r"Day048/Resources/ChromeDriver/chromedriver.exe"
WEB_LINK = "http://secure-retreat-92358.herokuapp.com/"

# Create a Options class, necessary to keep open the Chrome Browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path=CHROME_DRIVER_PATH)

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(WEB_LINK)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("cuong")
first_name.send_keys(Keys.ENTER)

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("phong")
last_name.send_keys(Keys.ENTER)

email = driver.find_element(By.NAME, "email")
email.send_keys("cuongphong2508@gmail.com")
email.send_keys(Keys.ENTER)

# driver.close()
# driver.quit()
