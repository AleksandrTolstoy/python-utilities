#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import time
from functools import wraps


def logged(time_format='%b %d %Y - %H:%M:%S', separator=''):
    def decorator(func):
        @wraps(func)
        def decorated_func(*args, **kwargs):
            arg_lst = []
            if args:
                arg_lst.append(', '.join(repr(arg) for arg in args))
            if kwargs:
                pairs = [f'{k}={w}' for k, w in sorted(kwargs.items())]
                arg_lst.append(', '.join(pairs))
            arg_str = ', '.join(arg_lst)

            print(f'{separator}- Running {func.__qualname__}({arg_str}) on {time.strftime(time_format)}')
            start_time = time.time()
            result = func(*args, **kwargs)
            print(f'- Finished {func.__qualname__}({arg_str}), execution time = {time.time() - start_time}s{separator}')
            return result
        return decorated_func
    return decorator

if __name__ == '__main__':
    @logged(separator='\n')
    def func(a, b, c, d=1, e=2):
        print('in func')

    func(1, 2, 3, **{'d':4, 'e':5})
    func(5, 4, 3)


