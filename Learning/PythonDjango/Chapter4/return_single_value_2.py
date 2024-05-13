# Created by tung.dao thanhtungpfiev@gmail.com at 5/12/2022
from functools import reduce
from operator import mul


def factorial(n):
    return reduce(mul, range(1, n + 1))


f5 = factorial(5)
