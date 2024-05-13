import os
import requests
from twilio.rest import Client

API_WEATHER = 'http://api.weatherapi.com/v1/forecast.json'
api_key = os.getenv('API_WEATHER_KEY')

account_sid = 'ACe7fa1979a8a7843e70ae7adcd314d51c'
auth_token = os.getenv('AUTH_TOKEN')

weather_params = {
    'q': 'Hanoi',
    'days': 2,
    'key': api_key,
    'aqi': 'no',
    'alerts': 'no'
}

response = requests.get(url=API_WEATHER, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_hours_check = weather_data['forecast']['forecastday'][1]['hour'][7:21]

will_it_rain = False
for hour_data in weather_hours_check:
    if hour_data['will_it_rain'] == 1:
        will_it_rain = True
        break

if will_it_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain tomorrow. Remember to bring an ☂️",
        from_='+13158030972',
        to='+84974351712'
    )

    print(message.status)
