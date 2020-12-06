class count_class():
    def __init__(self, number, step=1):
        self.number = number
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        current = self.number
        self.number += self.step
        return current