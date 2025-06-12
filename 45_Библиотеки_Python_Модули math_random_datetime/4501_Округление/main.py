import math

x = input()
n = float(x)
res = math.floor(n * 100 + 0.5 + 1e-9) / 100
print(res)