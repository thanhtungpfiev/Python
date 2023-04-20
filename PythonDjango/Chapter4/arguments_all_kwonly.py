# Created by Admin at 5/14/2022
def func_with_kwonly(a, b=42, *args, c, d=256, **kwargs):
    print('a, b:', a, b)
    print('c, d:', c, d)
    print('args:', args)
    print('kwargs:', kwargs)


func_with_kwonly(3, 1, c=0, d=1, *(7, 9, 11), e='E', f='F')
func_with_kwonly(3, 1, *(7, 9, 11), c=0, d=1, e='E', f='F')
