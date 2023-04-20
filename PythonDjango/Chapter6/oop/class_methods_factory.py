# Created by tung.dao thanhtungpfiev@gmail.com at 5/17/2022
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, coords):
        return cls(*coords)

    @classmethod
    def from_point(cls, point):
        return cls(point.x, point.y)


p = Point.from_tuple((3, 7))
print(p.x, p.y)

q = Point.from_point(p)
print(q.x, q.y)
