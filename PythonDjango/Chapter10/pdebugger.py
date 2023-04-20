# Created by Admin at 5/23/2022
d = {'first': 'v1', 'second': 'v2', 'fourth': 'v4'}
keys = ('first', 'second', 'third', 'fourth')


def do_something_with_value(value):
    print(value)


for key in keys:
    do_something_with_value(d[key])

print('Validation done.')
