# Created by Admin at 5/15/2022
def fibonacci(N):
    """Return all fibonacci numbers up to N. """
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b


print(list(fibonacci(0)))
print(list(fibonacci(1)))
print(list(fibonacci(50)))
