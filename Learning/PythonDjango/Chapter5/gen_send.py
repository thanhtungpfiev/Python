# Created by Admin at 5/15/2022
def counter(start=0):
    n = start
    while True:
        result = yield n
        print(type(result), result)
        if result == 'Q':
            break
        n += 1


c = counter()
print(next(c))
print(c.send('Wow!'))
print(next(c))
print(c.send('Q'))
