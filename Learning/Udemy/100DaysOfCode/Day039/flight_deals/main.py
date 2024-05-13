# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from datetime import datetime, timedelta

from notification_manager import NotificationManager
from flight_search import FlightSearch
from data_manager import DataManager

ORIGIN_CITY_IATA = "LON"

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

for data in sheet_data:
    if not data['iataCode']:
        data['iataCode'] = flight_search.get_destination_code(data['city'])
        data_manager.update_destination_code(data)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination['iataCode'],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight.price < destination['lowestPrice']:
        message = f"Low price alert! Only {flight.price} GBP to fly from {flight.origin_city}-{flight.origin_airport} " \
                  f"to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} " \
                  f"to {flight.return_date}."
        notification_manager.send_message(message.encode('utf-8'))
        # print(message)