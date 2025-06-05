def happy_number(n):
    s = n if isinstance(n, str) else str(n)
    if len(s) == 2:
        return [int(s[0]), int(s[1])]
    return [int(s[0]) + happy_number(s[1: -1])[0], int(s[-1]) + happy_number(s[1: -1])[1]]