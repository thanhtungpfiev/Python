# Created by Admin at 5/22/2022
import multiprocessing


def sum_and_product(a, b):
    s, p = a + b, a * b
    print(f'{a} + {b} = {s}, {a} * {b} = {p}')


if __name__ == '__main__':
    p = multiprocessing.Process(target=sum_and_product, name='SumProd', args=(7, 9))
    p.start()
