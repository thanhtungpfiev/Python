# Created by Admin at 5/18/2022
try:
    fh = open('fear.txt')
    for line in fh:
        print(line.strip())
finally:
    fh.close()
