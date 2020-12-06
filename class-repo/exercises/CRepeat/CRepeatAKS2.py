class repeat_class():
    def __init__(self, val, repeat_count=None):
        self.val = val
        self.repeat_count = repeat_count
    def __iter__(self):
        return self
    def __next__(self):
        if self.repeat_count is None:
            return self.val
        if self.repeat_count > 0:
            self.repeat_count -= 1
            return self.val
        raise StopIteration
