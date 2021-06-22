import requests

URL = 'https://opentdb.com/api.php'

parameters = {
    'amount' : 10,
    'type':'boolean',
}

data = requests.get(url=URL, params=parameters)
data.raise_for_status()

question_data = data.json()["results"]
