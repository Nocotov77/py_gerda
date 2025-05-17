import math


def trigonometric_function(mode, x, n):
    total = 0
    if mode == 'sin':
        for k in range(n + 1):
            total += (-1) ** k * (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
    elif mode == 'cos':
        for k in range(n + 1):
            total += (-1) ** k * (x ** (2 * k)) / math.factorial(2 * k)
    return total

data = ['sin', 1.57, 3]
print(trigonometric_function(*data))
