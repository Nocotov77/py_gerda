s = input()
d = {}
for x in map(lambda y: y.upper(), filter(lambda a: len(a) in (2, 3), s.split())):
    d[x] = d.get(x, 0) + 1
print(d)
