def mario(a, b):
    if a == 9:
        return 0
    if a == b:
        return 1
    if a < b:
        return 0
    res = mario(a - 1, b)
    if a % 2 == 0:
        res += mario(a // 2, b)
    return res