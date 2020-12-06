def repeat_while(val, num_times=None):
    while num_times is None or num_times > 0:
        if num_times is not None:
            num_times-=1
        yield val