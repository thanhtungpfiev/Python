import requests

APP_ID = "d2ecb310"
API_KEY = "ef766f7bc5bf5b1fdbbacddc293763d6"

EXERCISE_ENDPOINTS = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

request_body = {
    "query": "ran 3 miles",
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

response = requests.post(url=EXERCISE_ENDPOINTS, headers=headers, json=request_body)
print(response)
