# Created by Admin at 5/16/2022
class Point:
    x = 10
    y = 7


p = Point()
print(p.x)
print(p.y)

p.x = 12
print(p.x)
print(Point.x)

del p.x
print(p.x)

p.z = 3
print(p.z)

# print(Point.z)
