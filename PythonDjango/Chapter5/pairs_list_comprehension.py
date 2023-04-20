# Created by Admin at 5/15/2022
items = 'ABCD'
pairs = [(items[a], items[b]) for a in range(len(items)) for b in range(a, len(items))]
print(pairs)
