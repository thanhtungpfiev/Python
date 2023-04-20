# Created by Admin at 1/18/2022
data = [1, 2, 3, 4, 5, 6, 7, 8]
evens = []
for num in data:
    if not num % 2:
        evens.append(num)
print(evens)
evens_comp = [num for num in data if not num % 2]
print(evens_comp)

data = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
words = []
for num in data:
    if isinstance(num, str):
        words.append(num)
print(words)
words_comp = [num for num in data if isinstance(num, str)]
print(words_comp)

data = list('So long and thanks for all the fish'.split())
title = []
for word in data:
    title.append(word.title())
print(title)
title_comp = [word.title() for word in data]
print(title_comp)

vowels = {'a', 'e', 'i', 'o', 'u'}
message = "Don't forget to pack your towel."
found = set()
for v in vowels:
    if v in message:
        found.add(v)
print(found)

found2 = {v for v in vowels if v in message}
print(found2)