# Created by Admin at 5/18/2022
import os

with os.scandir('.') as it:
    for entry in it:
        print(entry.name, entry.path, 'File' if entry.is_file() else 'Folder')
