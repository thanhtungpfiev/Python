import requests

FLIGHT_DEALS_ENDPOINT = 'https://api.sheety.co/41b504e98a3b16098af3eda98fb2c93c/flightDeals/prices'


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=FLIGHT_DEALS_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_code(self, data):
        data_update = {
            "price": {
                "iataCode": data['iataCode']
            }
        }
        response = requests.put(url=f"{FLIGHT_DEALS_ENDPOINT}/{data['id']}", json=data_update)
