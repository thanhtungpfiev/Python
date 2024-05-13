# Created by tung.dao thanhtungpfiev@gmail.com at 5/13/2022
def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n)))
