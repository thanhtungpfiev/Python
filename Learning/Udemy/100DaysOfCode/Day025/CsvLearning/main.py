# with open('weather_data.csv') as weather_data_file:
#     data = weather_data_file.readlines()
#     print(data)

# import csv
#
# with open('weather_data.csv') as weather_data_file:
#     data = csv.reader(weather_data_file)
#     temperatures = []
#     for row in data:
#         if row[1] == 'temp':
#             pass
#         else:
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv('weather_data.csv')


# ? Get data in column
# print(data['temp'].mean())
# print(data['temp'].max())
#
# print(data.condition)


# ? Get data in row

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


# print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
monday_temp = convert_celsius_to_fahrenheit(int(monday.iloc[0].temp))
print(monday_temp)

# ? Create a data frame from scratch
data_dict = {
    "students": ['Amy', 'James', 'Angela'],
    "scores": [76, 56, 65]
}

data_new = pandas.DataFrame(data_dict)
data_new.to_csv('new_data.csv')
