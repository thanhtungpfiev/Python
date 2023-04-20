# Created by tung.dao thanhtungpfiev@gmail.com at 5/16/2022
from time import time, sleep
from functools import wraps


def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)

    return wrapper


@measure
def f(sleep_time=0.1):
    """I'm a cat. I love to sleep"""
    sleep(sleep_time)


f(sleep_time=0.3)
f(1)
f()
print(f.__name__, ':', f.__doc__)
