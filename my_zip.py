def my_zip(*args):
    iterators = [iter(item) for item in args]
    while iterators:
        result = []
        for item in iterators:
            try:
                element = next(item)
                result.append(element)
            except StopIteration:
                return
        yield tuple(result)
    return
