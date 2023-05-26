import requests

params = {
    "lat": 21.027763,
    "lng": 105.834160
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
