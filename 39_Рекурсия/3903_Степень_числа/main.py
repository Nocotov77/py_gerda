def power(x, p):
    if p == 0:
        return 1
    if p < 0:
        return 1 / power(x, -p)
    if p % 2 == 0:
        half = power(x, p // 2)
        return half * half
    return x * power(x, p - 1)