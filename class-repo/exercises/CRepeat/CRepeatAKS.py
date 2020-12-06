class repeat_class():
    def __init__(self, rep_data, time=None):
        self.rep_data = rep_data
        self.time = time
        self.counter = 0
    def __iter__(self) :
        return self
    def __next__(self):
        if self.time == None:
            return self.rep_data
        else:
            self.counter += 1
            if self.counter <= self.time:
                return self.rep_data
            else:
                raise StopIteration