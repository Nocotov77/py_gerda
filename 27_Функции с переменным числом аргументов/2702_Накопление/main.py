def accumulation(*args):
    s = 0
    res = [0]
    for x in args:
        s += x
        res.append(s)
    return res
data = [1, 2, 3, 4, 5]
print(*accumulation(*data))
