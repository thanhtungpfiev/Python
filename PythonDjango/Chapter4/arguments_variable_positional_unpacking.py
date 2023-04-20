# Created by Admin at 5/14/2022
def func(*args):
    print(args)


values = (1, 3, -7, 9)
func(values)  # equivalent to: func((1, 3, -7, 9))
func(*values)  # equivalent to: func(1, 3, -7, 9)
