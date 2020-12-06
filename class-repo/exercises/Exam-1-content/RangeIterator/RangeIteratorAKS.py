class range_iterator():
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.current != self.stop:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration

def range_iterator_while(start, stop):
    while start != stop:
        yield start
        start += 1
