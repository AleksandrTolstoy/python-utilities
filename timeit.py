import time
from contextlib import contextmanager


@contextmanager
def timeit(msg: str) -> None:
    '''Helps measure the execution time a part of code'''
    start_time = time.time()
    try:
        yield
    finally:
        print(f'{msg}: {time.time()- start_time}')


if __name__ == '__main__':
    from functools import reduce

    def xor(*args):
        return [reduce(lambda acum, el: acum ^ el, pair) for group in zip(*args) for pair in zip(*group)]

    with timeit('Test XOR'):
        a = [[1, 2], [3, 4]]
        b = [[3, 4], [1, 2]]
        print(xor(a, b))
