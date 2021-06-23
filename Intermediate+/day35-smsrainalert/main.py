import requests
from twilio.rest import Client
from private import LAT, LONG, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER,WEATHER_API_KEY, MY_NUMBER

def send_sms_alert():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
                    .create(
                        body="It's gonna rain todayyyy!!! \nTake an umbrella dudeee☔☔☔☔ \nMaybe take 4 :3",
                        from_=TWILIO_NUMBER,
                        to=MY_NUMBER
                    )
    print(message.sid)



WEATHER_URL = 'https://api.openweathermap.org/data/2.5/onecall'

WEATHER_PARAMETERS = {
    'lat': LAT,
    'lon': LONG,
    'appid': WEATHER_API_KEY,
    'exclude': "current,minutely,daily"
}

data = requests.get(url=WEATHER_URL, params=WEATHER_PARAMETERS)
data.raise_for_status()
weather_data = data.json()
hourly_data = weather_data["hourly"][:12]

for hour in hourly_data:
    condition_code = int(hour["weather"][0]["id"])
    if condition_code < 700:
        send_sms_alert()
        break
    else:
        print("Weather Good!")
