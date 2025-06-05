def opinions(*dicts):
    res = {}
    for d in dicts:
        for k, v in d.items():
            res.setdefault(k, set()).add(v)
    return res