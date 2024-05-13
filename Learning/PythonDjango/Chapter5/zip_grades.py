# Created by Admin at 5/14/2022
from alias import _
grades = [18, 23, 30, 27]
avgs = [22, 21, 29, 24]
print(_(zip(avgs, grades)))
print(_(map(lambda *a: a, avgs, grades)))
