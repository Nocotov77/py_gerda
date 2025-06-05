def accumulation(*args):
    s = 0
    res = [0]
    for x in args:
        s += x
        res.append(s)
    return res