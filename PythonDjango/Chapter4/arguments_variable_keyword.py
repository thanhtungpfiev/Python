# Created by tung.dao thanhtungpfiev@gmail.com at 5/11/2022
def func(**kwargs):
    print(kwargs)


func(a=1, b=42)
func(**{'a': 1, 'b': 42})
func(**dict(a=1, b=42))
