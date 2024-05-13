# Created by tung.dao thanhtungpfiev@gmail.com at 5/12/2022
def factorial(n):
    if n in (0, 1):
        return 1
    result = n
    for k in range(2, n):
        result *= k
    return result


f5 = factorial(5)
