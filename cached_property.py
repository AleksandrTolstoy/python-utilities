class cached_property:
    """Allows you to calculate attributes directly when they are accessed

    Useful for offloading object initialization
    """
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls=None):
        result = instance.__dict__[self.func.__name__] = self.func(instance)
        return result