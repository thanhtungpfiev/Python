# Created by Admin at 5/15/2022
A = 100
ex1 = [A for A in range(5)]
print(A)
ex2 = list(A for A in range(5))
print(A)
ex3 = dict((A, 2 * A) for A in range(5))
print(A)
ex4 = set(A for A in range(5))
print(A)
s = 0
for A in range(5):
    s += A
print(A)
