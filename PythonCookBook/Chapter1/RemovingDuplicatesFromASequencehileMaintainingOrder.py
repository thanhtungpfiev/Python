# Created by Admin at 5/9/2022
a = [1, 5, 2, 1, 9, 1, 5, 10]
set(a)

b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


list(dedupe(b, key=lambda d: (d['x'], d['y'])))
list(dedupe(b, key=lambda d: d['x']))
