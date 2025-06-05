m = int(input())
colors = [input().strip() for _ in range(m)]
k = int(input())

for i in range(k):
    print(colors[i % m])