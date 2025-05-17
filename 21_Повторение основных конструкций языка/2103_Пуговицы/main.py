n = int(input())
query = input()
k = int(input())
for i in range(1, k + 1):
    m = int(input())
    for _ in range(m):
        size = int(input())
        color = input()
        if size >= n and query in color:
            print(i, color, size)
