def my_reduce(*args):
    function = args[0]
    iterator = iter(args[1]) 
    if len(args) < 3 or args[2] == None:
        try:
            seed = next(iterator)
        except StopIteration:
            raise TypeError
    else:
        seed = args[2]
    val = seed
    for item in iterator:
       val = function(val, item)
    return val

