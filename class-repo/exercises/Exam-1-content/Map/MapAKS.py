def map_list(function, iterable):
    iterator = iter(iterable)
    output = []
    for item in iterator:
        output.append(function(item))
    return iter(output)

def map_while(function, iterable):
    iterator = iter(iterable)
    try:
        while True:
            yield function(next(iterator))
    except StopIteration:
        pass

def map_for(function, iterable):
    iterator = iter(iterable)
    for item in iterator:
        yield function(item)