def akscycle(iterable):
    while iterable:
        for item in iterable:
            yield item
    else:
        pass
def akscycle2(iterable):
    try:
        iterator = iter(iterable)
        while iterator:
            try:
                yield next(iterator)
            except StopIteration:
                iterator = iter(iterable)
                yield next(iterator)
    except:
        return