from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = r"Day048/Resources/ChromeDriver/chromedriver.exe"
WIKI_URL = "https://en.wikipedia.org/wiki/Main_Page"

# Create a Options class, necessary to keep open the Chrome Browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path=CHROME_DRIVER_PATH)

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(WIKI_URL)

articles_number = driver.find_element(By.CSS_SELECTOR, "#articlecount > a:nth-child(1)").text
print(articles_number)

driver.close()
driver.quit()
