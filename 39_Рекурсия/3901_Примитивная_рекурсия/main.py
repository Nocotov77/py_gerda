def func(n):
    if n == 0:
        return 0
    if n % 3 == 0:
        return func(n // 3) + 1
    return 2 + func(n - 1)