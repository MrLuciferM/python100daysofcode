import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from private import *


ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

driver_path = "D:/Learn/udemy/100daysofcode-python/chromedriver.exe"



response = requests.get(url=ZILLOW_URL,headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

# list addresses
address_tags = soup.select(".list-card-addr")
addresses = [tag.getText() for tag in address_tags]

# list prices
price_tags = soup.select(".list-card-price")
prices = [tag.getText() for tag in price_tags]

# list URLs
url_tags = soup.select(".list-card-info .list-card-link")
urls= []
for url in url_tags:
    href = url.get("href")
    if "http" not in href:
        urls.append(f"https://www.zillow.com{href}")
    else:
        urls.append(href)

# urls = [tag.get("href") for tag in url_tags]



driver = webdriver.Chrome(driver_path)

driver.get(GOOGLE_FORM_URL)




for i in range(len(addresses)):
    address_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    url_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
    address_box.send_keys(addresses[i])
    time.sleep(1)

    price_box.send_keys(prices[i])
    time.sleep(1)

    url_box.send_keys(urls[i])
    time.sleep(2)
    
    submit_btn.click()
    time.sleep(5)

    another_response = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()
    time.sleep(5)
print("done")

driver.quit()