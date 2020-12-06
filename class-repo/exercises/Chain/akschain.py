def akschain(*args):
    chain = []
    for iterable in args:
        for item in iterable:
            chain.append(item)
    return chain

def akschaingen(*args):
    return (item for iterable in args for item in iterable)