# Created by Admin at 5/15/2022
from time import time
mx = 5000

t = time()
floop = []
for a in range(1, mx):
    for b in range(a, mx):
        floop.append(divmod(a, b))
print('for loop: {:.4f}s'.format(time() - t))

t = time()
compr = [divmod(a, b) for a in range(1, mx) for b in range(a, mx)]
print('list comprehension: {:.4f}s'.format(time() - t))

t = time()
gen = list(divmod(a, b) for a in range(1, mx) for b in range(a, mx))
print('generator expression: {:.4f}s'.format(time() - t))
