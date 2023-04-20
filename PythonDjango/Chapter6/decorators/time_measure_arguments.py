# Created by tung.dao thanhtungpfiev@gmail.com at 5/16/2022
from time import sleep, time


def f(sleep_time=0.1):
    sleep(sleep_time)


def measure(func, *args, **kwargs):
    t = time()
    func(*args, **kwargs)
    print(func.__name__, 'took:', time() - t)


measure(f, sleep_time=0.3)
measure(f, 0.2)
