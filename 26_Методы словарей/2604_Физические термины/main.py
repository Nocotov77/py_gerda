d = {}
while True:
    s = input()
    if s == "":
        break
    k, v = s.split(": ")
    d[v] = k
n = int(input())
for _ in range(n):
    q = input()
    print(d.get(q))
