# Created by Admin at 5/15/2022
from functions import gcd
from time import time


def gen_triples(N):
    for m in range(1, int(N ** 0.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 and gcd(m, n) == 1:
                c = m ** 2 + n ** 2
                if c <= N:
                    a = m ** 2 - n ** 2
                    b = 2 * m * n
                    yield a, b, c


t = time()
triples = sorted(gen_triples(5000000), key=lambda *triple: sum(*triple))
print('{:.4f}'.format(time() - t))
