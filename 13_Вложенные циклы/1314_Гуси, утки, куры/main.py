n = int(input())
m = int(input())

found = False
max_g = min(n, m // 25)

for g in range(max_g + 1):
    remaining_m = m - 25 * g
    remaining_n = n - g

    if remaining_n < 0 or remaining_m < 0:
        continue

    numerator = remaining_m - 7 * remaining_n
    if numerator < 0 or numerator % 3 != 0:
        continue

    d = numerator // 3
    c = remaining_n - d

    if d >= 0 and c >= 0:
        print(g, d, c)
        found = True

if not found:
    pass