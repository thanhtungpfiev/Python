import requests

params = {
    'lat': 21.027763,
    'lng': 105.834160,
    'formatted': 0
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=params)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

print(sunrise, sunset)
