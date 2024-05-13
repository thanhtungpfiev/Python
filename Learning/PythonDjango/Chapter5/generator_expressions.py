# Created by Admin at 5/15/2022
cubes = [k**3 for k in range(10)]
print(cubes)
print(type(cubes))
cubes_gen = (k**3 for k in range(10))
print(cubes_gen)
print(type(cubes_gen))
print(list(cubes_gen))
print(list(cubes_gen))
