# Created by Admin at 5/15/2022
from alias import _

squares = []
for n in range(10):
    squares.append(n ** 2)
print(squares)

squares1 = map(lambda n1: n1 ** 2, range(10))
print(_(squares1))
