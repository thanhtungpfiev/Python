# Created by Admin at 5/15/2022
def adder(*n):
    return sum(n)


s1 = sum(map(lambda *n: adder(*n), range(100), range(1, 101)))
print(s1)
s2 = sum(adder(*n) for n in zip(range(100), range(1, 101)))
print(s2)
