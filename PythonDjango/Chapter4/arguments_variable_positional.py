# Created by tung.dao thanhtungpfiev@gmail.com at 5/11/2022
def minimum(*n):
    if n:
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)


minimum(1, 3, -7, 9)
minimum()
