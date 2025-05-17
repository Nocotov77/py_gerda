n = int(input())
m = int(input())
elements = [input().strip() for _ in range(n * m)]

matrix = []
for i in range(n):
    start = i * m
    end = start + m
    matrix.append(elements[start:end])

for row in matrix:
    print('; '.join(row))

print()

transposed = zip(*matrix)

for row in transposed:
    print('; '.join(row))