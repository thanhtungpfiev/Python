from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = r"Day048/Resources/ChromeDriver/chromedriver.exe"
PRODUCT_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
PYTHON_URL = "https://www.python.org/"

# Create a Options class, necessary to keep open the Chrome Browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path=CHROME_DRIVER_PATH)

driver = webdriver.Chrome(service=service, options=chrome_options)

# driver.maximize_window()
#
# driver.get(PRODUCT_URL)
#
# price = driver.find_element(By.XPATH,
#                             '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]/span[1]')
# print(price.get_attribute("textContent"))

# driver.get(PYTHON_URL)
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))

driver.get(PYTHON_URL)

upcoming_events_times = driver.find_elements(By.CSS_SELECTOR,
                                             "#content > div > section > div.list-widgets.row > "
                                             "div.medium-widget.event-widget.last > div > ul > li > time")
upcoming_events_names = driver.find_elements(By.CSS_SELECTOR,
                                             "#content > div > section > div.list-widgets.row > "
                                             "div.medium-widget.event-widget.last > div > ul > li > a")
# event_data = {}
# for i in range(len(upcoming_events_times)):
#     time = upcoming_events_times[i].get_attribute("datetime").split('T')[0]
#     name = upcoming_events_names[i].text
#     event_data[i] = {'time': time, 'name': name}

# comprehension
event_data = {i: {upcoming_events_times[i].get_attribute("datetime").split('T')[0]: upcoming_events_names[i].text} for i
              in range(len(upcoming_events_names))}

print(event_data)

driver.close()
driver.quit()
