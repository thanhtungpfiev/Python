# Created by Admin at 5/22/2022
import threading
from time import sleep


def print_current():
    print('The current thread is {}.'.format(threading.currentThread()))
    print('Threads: {}'.format(list(threading.enumerate())))


def status(t):
    if t.is_alive():
        print(f'Thread {t.name} is alive.')
    else:
        print(f'Thread {t.name} has terminated')


def sum_and_product(a, b):
    sleep(.2)
    print_current()
    s, p = a + b, a * b
    print(f'{a} + {b} = {s}, {a} * {b} = {p}')


print_current()
t = threading.Thread(target=sum_and_product, name='SumPro', args=(3, 7))
t.start()
status(t)
t.join()
status(t)
