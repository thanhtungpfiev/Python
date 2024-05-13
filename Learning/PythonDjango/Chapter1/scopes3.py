# Created by Admin at 5/14/2022
def enclosing_func():
    m = 13

    def local():
        print(m, 'printing from the local scope')

    local()


m = 5
print(m, 'printing from the global scope')
enclosing_func()
