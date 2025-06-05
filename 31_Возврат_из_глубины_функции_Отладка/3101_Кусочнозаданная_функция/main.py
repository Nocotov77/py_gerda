def definition(x):
    if x <= 0:
        return x ** 2 + 2 * x
    if 0 < x <= 2:
        return x
    if 2 < x <= 4:
        return 4
    if x > 4:
        return 8 / x