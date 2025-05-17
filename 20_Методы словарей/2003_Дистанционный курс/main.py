n = int(input())
d = {}
for _ in range(n):
    line = input()
    name, score = line.split(": ")
    d[name] = d.get(name, 0) + int(score)
for name, total in d.items():
    if total >= 75:
        print(name)
