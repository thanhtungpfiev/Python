# Created by Admin at 5/15/2022
from alias import _
cubes = [x**3 for x in range(10)]
odd_cubes1 = _(filter(lambda cube: cube % 2, cubes))
odd_cubes2 = _(cube for cube in cubes if cube % 2)
