# Created by Admin at 5/18/2022
import os
filename = 'fear.txt'
path = os.path.dirname(os.path.abspath(filename))
print(os.path.isfile(filename))
print(os.path.isdir(path))
print(path)
