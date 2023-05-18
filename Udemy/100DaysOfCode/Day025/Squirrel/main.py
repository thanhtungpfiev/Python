import numpy as np
import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
color_list = data['Primary Fur Color'].tolist()
color_set = set(color_list)
color_dict = {}
new_color_list = []
new_count = []
for color in color_set:
    new_color_list.append(color)
    new_count.append(color_list.count(color))

color_dict['Fur Color'] = new_color_list
color_dict['Count'] = new_count

new_data = pandas.DataFrame(color_dict)
new_data_file = new_data.to_csv('squirrel_count.csv')
