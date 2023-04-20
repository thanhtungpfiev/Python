# Created by Admin at 5/8/2022
from collections import OrderedDict

d = {'foo': 1, 'bar': 2, 'spam': 3, 'grok': 4}
for key in d:
    print(key, d[key])


e = OrderedDict()
e['foo'] = 1
e['bar'] = 2
e['spam'] = 3
e['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in e:
    print(key, e[key])
