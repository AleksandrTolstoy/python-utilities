from collections import deque

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

    def __call__(self, fn):
        def wrapped(*args, **kwargs):
            memoization_key = self._convert_call_arguments_to_hash(args, kwargs)
            if memoization_key not in self.call_args_to_result:
                result = fn(*args, **kwargs)
                self._update_cache_key_with_value(memoization_key, result)
                self._evict_cache_if_necessary()
            return self.call_args_to_result[memoization_key]
        return wrapped

if __name__ == '__main__':
    @Memoized()
    def fib(n):
        if n < 2:
            return n
        return fib(n-2) + fib(n-1)

    @Memoized()
    def sec_fib(n):
        a, b = 1, 1
        for i in range(n):
            yield b
            a, b = b, a + b

    print(f'fib(200) = {fib(900)}')
    print(f'fib(180) = {fib(600)}')

    for i in sec_fib(10):
        print(i)