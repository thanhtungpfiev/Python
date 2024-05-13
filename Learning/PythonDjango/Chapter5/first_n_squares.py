# Created by Admin at 5/15/2022
def get_squares(n):
    return [x ** 2 for x in range(10)]


print(get_squares(10))


def get_squares_gen(n):
    for x in range(n):
        yield x ** 2


print(list(get_squares_gen(10)))
