# Created by Admin at 5/15/2022
def gcd(a, b):
    """Calculate the Greatest Common Divisor of (a, b)"""
    while b != 0:
        a, b = b, a % b
    return a
