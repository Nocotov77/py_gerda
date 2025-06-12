import math


def multiplier(*args, key):
    lst = [x for x in args if key(x)]
    return math.prod(lst) if lst else None