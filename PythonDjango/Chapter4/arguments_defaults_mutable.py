# Created by Admin at 5/14/2022
def func(a=[], b={}):
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a))
    b[len(a)] = len(a)


# func()
# func()
# func()
func()
func(a=[1, 2, 3], b={'B': 1})
func()
