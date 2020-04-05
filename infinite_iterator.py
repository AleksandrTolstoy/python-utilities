#!/usr/bin/python3
# -*- coding: UTF-8 -*-


class InfiniteAddition:
    """Provides infinite sequential addition 1 to given number"""

    def __init__(self, initial_number):
        """Start value announced"""
        self.number_to_add = initial_number

    def __iter__(self):
        """This method allows you to return itself when passing the object
         to the <iter> function, thereby accurately implementing the iterator protocol"""
        return self

    def __next__(self):
        """Update the value and return the result"""
        self.number_to_add = self.number_to_add + 1
        return self.number_to_add


if __name__ == '__main__':
    start = InfiniteAddition(3)
    for next_ in start:
        print(next_)
