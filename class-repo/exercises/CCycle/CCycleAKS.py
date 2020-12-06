class cycle_class():
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(self.iterable)
    def __iter__(self):
        return self
    def __next__(self):
        try:
            next_val = next(self.iterator)
            return next_val
        except StopIteration:
            self.iterator = iter(self.iterable)
            next_val = next(self.iterator)
            return next_val