# Created by tung.dao thanhtungpfiev@gmail.com at 5/17/2022
class A:
    label = 'a'


class B(A):
    pass


class C(A):
    label = 'c'


class D(B, C):
    pass


d = D()
print(d.label)
print(d.__class__.mro())
