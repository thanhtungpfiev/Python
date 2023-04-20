# Created by tung.dao thanhtungpfiev@gmail.com at 5/11/2022
def kwo(*a, c):
    print(a, c)


kwo(1, 2, 3, c=7)
kwo(c=4)


def kwo2(a, b=42, *, c):
    print(a, b, c)


kwo2(3, b=7, c=99)
kwo2(3, c=13)
kwo2(3, 23, c=25)
