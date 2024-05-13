# Created by Admin at 5/14/2022
from alias import _

a = [5, 9, 2, 4, 7]
b = [3, 7, 1, 9, 2]
c = [6, 8, 0, 5, 3]

d = zip(a, b, c)
e = map(lambda n: max(*n), d)
print(_(e))
