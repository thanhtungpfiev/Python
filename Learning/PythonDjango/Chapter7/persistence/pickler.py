# Created by Admin at 5/19/2022
import pickle
from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    id: int

    def greet(self):
        print(f'Hi, I am {self.first_name} {self.last_name}'
              f' and my ID is {self.id}')


people = [
    Person('Obi-Wan', 'Kenobi', 123),
    Person('Anakin', 'Skywalker', 456),
]

with open('data.pickle', 'wb') as stream:
    pickle.dump(people, stream)

with open('data.pickle', 'rb') as stream:
    peeps = pickle.load(stream)

for person in peeps:
    print(person)
