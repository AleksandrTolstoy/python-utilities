#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import time
import logging
from collections import deque
from functools import wraps


class Memoized:

    def __init__(self, cache_size=1024):
        self.cache_size = cache_size
        self.call_args_queue = deque()
        self.call_args_to_result = {}

    def _update_cache_key_with_value(self, key, value):
        self.call_args_to_result[key] = value
        self.call_args_queue.append(key)

    def _evict_cache_if_necessary(self):
        if len(self.call_args_queue) > self.cache_size:
            oldest_key = self.call_args_queue.popleft()
            del self.call_args_to_result[oldest_key]

    @staticmethod
    def _convert_call_arguments_to_hash(args, kwargs):
        return hash(str(args) + str(kwargs))

    def __call__(self, func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            memoization_key = self._convert_call_arguments_to_hash(args, kwargs)
            start_time = time.time()
            if memoization_key not in self.call_args_to_result:
                result = func(*args, **kwargs)
                self._update_cache_key_with_value(memoization_key, result)
                self._evict_cache_if_necessary()
            logging.debug(f'Execution time = {time.time() - start_time}s')
            return self.call_args_to_result[memoization_key]
        return wrapped


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.DEBUG, datefmt='%H:%M:%S') # or INFO

    @Memoized()
    def fib(n):
        if n < 2:
            return n
        return fib(n - 2) + fib(n - 1)

    start_time = time.time()
    print(f'Memoized recursive fib(40) = {fib(40)}')
    print(f'Execution time = {time.time() - start_time}s')

    start_time = time.time()
    print(f'Memoized recursive fib(20) = {fib(20)}')
    print(f'Execution time = {time.time() - start_time}s\n')

    def fib(n):
        if n < 2:
            return n
        return fib(n - 2) + fib(n - 1)

    start_time = time.time()
    print(f'Recursive fib(40) = {fib(40)}')
    print(f'Execution time = {time.time() - start_time}s')

    start_time = time.time()
    print(f'Recursive fib(20) = {fib(20)}')
    print(f'Execution time = {time.time() - start_time}s\n')

    @Memoized()
    def fib(n):
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return b

    start_time = time.time()
    print(f'Memoized fib(900) = {fib(900)}')
    print(f'Execution time = {time.time() - start_time}s')

    start_time = time.time()
    print(f'Memoized fib(800) = {fib(800)}')
    print(f'Execution time = {time.time() - start_time}s\n')

    def fib(n):
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return b

    start_time = time.time()
    print(f'fib(900) = {fib(900)}')
    print(f'Execution time = {time.time() - start_time}s')

    start_time = time.time()
    print(f'fib(800) = {fib(800)}')
    print(f'Execution time = {time.time() - start_time}s\n')
