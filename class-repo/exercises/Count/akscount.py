def count_while(val, step=1):
    while val:
        yield val
        val = val + step
    else:
        return