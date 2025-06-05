n = int(input())
m = int(input())
p = int(input())

if n > p:
    m *= -1
    p -= 1
else:
    p += 1

for i in range(n, p, m):
    print(f"Высота {i}")

print("Глиссада")