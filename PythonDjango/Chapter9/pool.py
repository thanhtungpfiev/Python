# Created by Admin at 5/22/2022
from concurrent.futures import ThreadPoolExecutor, as_completed
from random import randint
import threading
from time import sleep


def run(name):
    sleep(.05)
    value = randint(0, 10 ** 2)
    tname = threading.current_thread().name
    print(f'Hi, I am {name} ({tname}) and my value is {value}')
    return (name, value)


with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [
        executor.submit(run, f'T{name}') for name in range(5)
    ]
    for future in as_completed(futures):
        name, value = future.result()
        print(f'Thread {name} returned {value}')
