class SkipIterator:

    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 1
            return item

class SkipObject:

    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        """Each call returns a new iterator object"""
        return SkipIterator(self.wrapped)

if __name__ == '__main__':
    alpha = 'abc'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I), next(I), next(I))

    for x in skipper:
        for y in skipper:
            print(x + y, end=' ')
