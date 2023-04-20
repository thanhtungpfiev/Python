# Created by Admin at 5/15/2022
def get_squares_gen(n):
    for x in range(n):
        yield x ** 2


squares = get_squares_gen(4)
print(squares)
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
