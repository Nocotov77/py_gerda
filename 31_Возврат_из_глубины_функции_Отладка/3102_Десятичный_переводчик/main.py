def decimal_translator(number, base):
    s = str(number)
    total = 0
    for ch in s:
        d = int(ch)
        if d >= base:
            return None
        total = total * base + d
    return total