import os
from datetime import datetime

import requests

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

QUERY = input("Tell me which exercises you did: ")
GENDER = "male"
WEIGHT_KG = 64.5
HEIGHT_CM = 170
AGE = 33

nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

nutri_request_body = {
    "query": QUERY,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=EXERCISE_ENDPOINT, headers=nutri_headers, json=nutri_request_body)
exercises = response.json()["exercises"]

for exercise in exercises:
    SHEETY_ADD_ROW_ENDPOINT = os.getenv("SHEETY_ADD_ROW_ENDPOINT")

    sheety_request_body = {
        "workout": {
            "date": datetime.today().date().strftime("%d/%m/%Y"),
            "time": datetime.today().time().strftime("%H:%M:%S"),
            "exercise": exercise["name"].song(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_headers = {
        "Authorization": os.getenv("TOKEN")
    }

    response = requests.post(url=SHEETY_ADD_ROW_ENDPOINT, headers=sheety_headers, json=sheety_request_body)
    print(response.text)
