# Created by Admin at 5/15/2022
from string import ascii_lowercase
letter_map = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))
print(letter_map)
letter_map1 = {c: k for k, c in enumerate(ascii_lowercase, 1)}
print(letter_map1)
