# Created by Admin at 5/8/2022
greet_old = 'Hello %s!'
greet_old % 'Fabrizio'

greet_positional = 'Hello {} {}!'
greet_positional.format('Fabrizio', 'Romano')

greet_positional_idx = 'This is {0}! {1} loves {0}!'
greet_positional_idx.format('Python', 'Fabrizio')
greet_positional_idx.format('Coffee', 'Fab')

keyword = 'Hello, my name is {name} {last_name}'
keyword.format(name='Fabrizio', last_name='Romano')

name = 'Fab'
age = 42
f"Hello! My name is {name} and I'm {age}"
