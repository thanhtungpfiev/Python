# Created by tung.dao thanhtungpfiev@gmail.com at 5/17/2022
class A:
    def __init__(self, factor):
        self._factor = factor

    def op1(self):
        print('Op1 with factor {}...'.format(self._factor))


class B(A):
    def op2(self, factor):
        self._factor = factor
        print('Op2 with factor {}...'.format(self._factor))


obj = B(100)
obj.op1()
obj.op2(42)
obj.op1()

print(obj.__dict__.keys())
