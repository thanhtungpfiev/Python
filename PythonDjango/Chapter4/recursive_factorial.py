# Created by tung.dao thanhtungpfiev@gmail.com at 5/13/2022
def factorial(n):
    if n in (0, 1):
        return 1
    return factorial(n - 1) * n


ft5 = factorial(5)
