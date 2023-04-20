# Created by Admin at 5/14/2022
from alias import _

print(_(map(lambda *a: a, range(3))))
print(_(map(lambda *a: a, range(3), 'abc')))
print(_(map(lambda *a: a, range(3), 'abc', range(4, 7))))
print(_(map(lambda *a: a, (), 'abc')))
print(_(map(lambda *a: a, (1, 2), 'abc')))
print(_(map(lambda *a: a, (1, 2, 3, 4), 'abc')))
