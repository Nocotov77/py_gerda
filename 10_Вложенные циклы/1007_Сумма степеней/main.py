n = int(input())
original = n
factors = []
d = 2

while d * d <= n:
    while n % d == 0:
        factors.append(d)
        n = n // d
    d += 1
if n > 1:
    factors.append(n)

print(f"{original} = {' * '.join(map(str, factors))}")