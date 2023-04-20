# Created by Admin at 5/14/2022
def local():
    print(m, 'printing from the local scope')


m = 5
print(m, 'printing from the global scope')
local()
