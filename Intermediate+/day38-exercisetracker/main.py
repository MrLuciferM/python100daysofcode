import requests
from datetime import datetime

NEUTRINIX_KEY = "13c428dee40d002614e157bc4a19213f"
NEUTRINIX_APPID = "9c5f88ad"

GENDER = "male"
WEIGHT_KG = 55
HEIGHT_CM = 170
AGE = 21

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

neutrinix_headers = {
    "x-app-id": NEUTRINIX_APPID,
    "x-app-key": NEUTRINIX_KEY,
    # "x-remote-user-id": 0
}

parameters = {
    "query": input("What workout did you do today? "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=neutrinix_headers)
# print(response.json())

exercise_data = response.json()["exercises"]

sheety_endpoint = "https://api.sheety.co/7e71ed13f385fb86dd4416dea0eb2f08/workoutTracker/workouts"

sheety_headers = {
    "Authorization": "Bearer HJFA5BSN3BFALK5ELMF4KEOSERN"
}

# read from google sheet

# response = requests.get(url=sheety_endpoint, headers=sheety_headers)
# response.raise_for_status()
# print(response.json())


# post workouts in google sheet
for exercise in exercise_data:    
    workouts = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(url=sheety_endpoint,json=workouts, headers=sheety_headers)
    print(response.json())


# print(workouts)