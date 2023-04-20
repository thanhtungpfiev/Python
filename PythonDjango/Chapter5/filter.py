# Created by Admin at 5/14/2022
from alias import _
test = [2, 5, 8, 0, 0, 1, 0]
test1 = _(filter(None, test))
test2 = _(filter(lambda x: x, test))
test3 = _(filter(lambda x: x > 4, test))
