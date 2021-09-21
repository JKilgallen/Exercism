def flatten(iterable):
    out = []
    for x in iterable:
        if x is None:
            pass
        elif type(x) == list:
            out += flatten(x)
        else:
            print(x)
            out.append(x)
    
    return out
