a, b, c = (input() for _ in range(3))
result = (a < b and a or b) < c and (a < b and a or b) or c
print(result)