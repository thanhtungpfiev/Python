# Created by Admin at 5/15/2022
def fibonacci(N):
    """Return all fibonacci numbers up to N. """
    result = [0]
    next_n = 1
    while next_n <= N:
        result.append(next_n)
        next_n = sum(result[-2:])
    return result


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(50))
