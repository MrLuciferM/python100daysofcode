from selenium import webdriver

chrome_driver_path = "D:/Learn/udemy/100daysofcode-python/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

event_dates = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

events = [
    {
        date.text: title.text
    }
    for date, title in zip(event_dates, event_names)
    ]

print(events)

driver.quit()