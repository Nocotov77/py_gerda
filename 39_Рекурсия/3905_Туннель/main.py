def tunnel(lst):
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return lst[0] + lst[1]
    return tunnel(lst[1: -1])