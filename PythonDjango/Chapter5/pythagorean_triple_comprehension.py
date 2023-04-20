# Created by Admin at 5/15/2022
from math import sqrt
mx = 10
triples = [(a, b, sqrt(a ** 2 + b ** 2)) for a in range(1, mx) for b in range(a, mx)]
triples = [(a, b, int(c)) for a, b, c in triples if c.is_integer()]
print(triples)
