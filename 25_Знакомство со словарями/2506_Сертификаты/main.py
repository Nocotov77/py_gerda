n = int(input())
d = {}
for _ in range(n):
    a = input().split()
    d[a[0]] = (int(a[1]), int(a[2]))
s = sum(map(int, input().split()))
for k, (low, high) in d.items():
    if low <= s <= high:
        print(k)
        break
