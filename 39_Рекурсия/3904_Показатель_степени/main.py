def degree_indicator(num, base):
    if num == 1:
        return 0
    if num < 1:
        return degree_indicator(num * base, base) - 1
    return degree_indicator(num / base, base) + 1