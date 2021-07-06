import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
from private import *

product_url = "https://www.amazon.com/LG-29WP60G-B-Inch-Connectivity-Borderless/dp/B08V86LGBS/"



def send_alert(product,price):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIEVER_EMAIL,
            msg=f"Subject: Amazon Price Drop Alert\n\n{product} is now {price} \nORDER NOW:\n{product_url}"
        )
        print("alert sent successfully")

response = requests.get(url=product_url, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")
price_dollars = soup.select_one(selector="#priceblock_ourprice").getText().strip()
product_title = soup.select_one(selector="#productTitle").getText().strip()
price_amt = float(price_dollars.lstrip("$"))

if price_amt < 200:
    send_alert(product_title, price_dollars)
