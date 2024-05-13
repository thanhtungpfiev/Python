# Created by Admin at 1/16/2022
import csv
import pprint
from datetime import datetime


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as data:
    for line in csv.reader(data):
        print(line)

with open('buzzers.csv') as data:
    for line in csv.DictReader(data):
        print(line)

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v
    pprint.pprint(flights)
    print()

    flights2 = {}
    for k, v in flights.items():
        flights2[convert2ampm(k)] = v.title()
    pprint.pprint(flights2)
    more_flights = {convert2ampm(k): v.title() for k, v in flights.items()}
    pprint.pprint(more_flights)
    just_freeport = {}
    for k, v in flights.items():
        if v == 'FREEPORT':
            just_freeport[convert2ampm(k)] = v.title()
    pprint.pprint(just_freeport)
    just_freeport2 = {convert2ampm(k): v.title() for k, v in flights.items() if v == 'FREEPORT'}
    pprint.pprint(just_freeport2)
    just_freeport3 = {convert2ampm(k): v.title()
                      for k, v in flights.items()
                      if v == 'FREEPORT'}
    pprint.pprint(just_freeport3)

    flight_time = []
    for ft in flights.keys():
        flight_time.append(convert2ampm(ft))
    print(flight_time)
    more_flight_time = [convert2ampm(ft) for ft in flights.keys()]
    print(more_flight_time)

    destinations = []
    for dest in flights.values():
        destinations.append(dest.title())
    print(destinations)

    more_dest = [dest.title() for dest in flights.values()]
    print(more_dest)

    fts = {convert2ampm(k): v.title() for k, v in flights.items()}
    when = {}
    for dest in set(fts.values()):
        when[dest] = [k for k, v in fts.items() if v == dest]
    pprint.pprint(when)
    when2 = {dest: [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}
    pprint.pprint(when2)
