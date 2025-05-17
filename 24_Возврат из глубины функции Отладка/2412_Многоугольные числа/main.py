def create_polygon_number(n, q):
    return ((q - 2) * n**2 - (q - 4) * n) // 2


def check_polygon_number(number):
    import math
    if number == 1:
        return (1, 3)
    best = None
    best_n = -1
    max_n = int((math.sqrt(1 + 8 * number) - 1) // 2)
    for n in range(2, max_n + 1):
        denom = n * (n - 1)
        num = 2 * (number + n ** 2 - 2 * n)
        if denom != 0 and num % denom == 0:
            q = num // denom
            if q >= 3 and n > best_n:
                best_n = n
                best = (n, q)
    return best if best is not None else (None, None)

print(check_polygon_number(70))
print(check_polygon_number(2))
print(check_polygon_number(81))
print(create_polygon_number(5, 8))