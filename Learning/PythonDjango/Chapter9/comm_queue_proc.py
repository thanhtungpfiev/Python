# Created by Admin at 5/22/2022
import multiprocessing

SENTINEL = 'STOP'


def producer(q, n):
    a, b = 0, 1
    while a <= n:
        q.put(a)
        a, b = b, a + b
    q.put(SENTINEL)


def consumer(q):
    while True:
        num = q.get()
        if num == SENTINEL:
            break
        print(f'Got number {num}')


if __name__ == '__main__':
    q = multiprocessing.Queue()
    cns = multiprocessing.Process(target=consumer, args=(q,))
    prd = multiprocessing.Process(target=producer, args=(q, 35))
    cns.start()
    prd.start()
