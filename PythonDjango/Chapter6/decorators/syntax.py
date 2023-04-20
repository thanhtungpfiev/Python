# Created by tung.dao thanhtungpfiev@gmail.com at 5/16/2022
# # one decorator
# def func(arg1, arg2, ...):
#     pass
#
#
# func = decorator(func)
#
#
# # is equivalent to the following:
# @decorator
# def func(arg1, arg2, ...):
#     pass
#
#
# def func(arg1, arg2, ...):
#     pass
#
#
# # two decorator
# func = deco1(deco2(func))
#
#
# # is equivalent to the following:
# @deco1
# @deco2
# def func(arg1, arg2, ...):
#     pass
#
#
# def func(arg1, arg2, ...):
#     pass
#
#
# # one decorator that takes arguments
# func = decoarg(arg_a, arg_b)(func)
#
#
# # is equivalent to the following:
# @decoarg(arg_a, arg_b)
# def func(arg1, arg2, ...):
#     pass
