import requests
from datetime import date, timedelta
from private import *
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

def send_sms_alert(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
                    .create(
                        body=message,
                        from_=TWILIO_NUMBER,
                        to=MY_NUMBER
                    )
    print(message.sid)

today = date.today()
# yesterday_date = today-timedelta(days=1)
# day_before_yesterday_date = today-timedelta(days=2)

parameters = {
    'function' : 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'outputsize': 'compact',
    'apikey': STOCK_KEY,
}

data = requests.get(url=STOCK_ENDPOINT, params=parameters)
data.raise_for_status()

stock_data = data.json()["Time Series (Daily)"]

data_list = [value for (key,value) in stock_data.items()]

# yesterday_closing = float(stock_data[str(yesterday_date)]["4. close"])
yesterday_closing = float(data_list[0]["4. close"])

# dbfr_yesterday_closing = float(stock_data[str(day_before_yesterday_date)]["4. close"])
dbfr_yesterday_closing = float(data_list[1]["4. close"])


difference = yesterday_closing-dbfr_yesterday_closing

if difference > 0:
    direction = "🔺"
elif difference < 0:
    direction = "🔻"
else:
    difference = "⏸"

percentage_difference = round((abs(difference) / dbfr_yesterday_closing)*100,2)




if percentage_difference > 5:
    print("Great News!!")
    
    parameters = {
        'apiKey': NEWS_KEY,
        'q': COMPANY_NAME,
        'from': str(today - timedelta(days=3)),
        'language': 'en',
        'sortBy':'relevancy'
    }
    
    data = requests.get(url=NEWS_ENDPOINT, params=parameters)
    data.raise_for_status()

    articles = data.json()["articles"][:3]

    for each in articles:
        title = each["title"]
        brief = each["description"]
        source = each["url"]
        message = f"{STOCK_NAME}: {direction} {percentage_difference}%\nHeadline: {title}\nBrief: {brief}\nSource: {source}"
        send_sms_alert(message)
        # print(message)
else:
    print("Not a big difference")
