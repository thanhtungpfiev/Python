import os
import smtplib

import requests
from bs4 import BeautifulSoup

PRODUCT_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
}

MY_PRICE = 100

product_website = requests.get(url=PRODUCT_URL, headers=HEADERS).text
soup = BeautifulSoup(product_website, "html.parser")
# print(soup.prettify())

title = soup.find(id="productTitle").get_text().strip()

price = float(soup.find(
    "span", class_="a-offscreen").getText().split("$")[1])

MY_EMAIL = "cuongphong2508@gmail.com"
MY_PASSWORD = os.getenv("MY_PASSWORD")

if price < MY_PRICE:
    message = f"{title} is now {price}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="thanhtungpfiev@gmail.com",
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{PRODUCT_URL}".encode("utf-8"))
