class range_iterator():
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        val = self.current
        if val < self.stop:
            self.current += self.step
            return val
        else:
            self.current = self.start
            raise StopIteration