from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "https://secure-retreat-92358.herokuapp.com/"
chrome_driver_path = "D:/Learn/udemy/100daysofcode-python/chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get(URL)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Kunal")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Gupta")

email = driver.find_element_by_name("email")
email.send_keys("someemail@gmail.com")

signup = driver.find_element_by_css_selector("button")

signup.click()

success = driver.find_element_by_class_name("display-3")

print(success.text)

driver.quit()