# Created by Admin at 5/16/2022
class Person:
    species = 'Human'


print(Person.species)
Person.alive = True
print(Person.alive)

man = Person()
print(man.species)
print(man.alive)

man.name = 'Darth'
man.surname = 'Varder'
print(man.name, man.surname)
