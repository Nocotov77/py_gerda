def opinions(*dicts):
    res = {}
    for d in dicts:
        for k, v in d.items():
            res.setdefault(k, set()).add(v)
    return res

data = [{'f': 1, 's': 2}, {'s': 2, 't': 3},
        {'s': 3, 'f': 5}, {'f': 4}, {}]
print(opinions(*data))
