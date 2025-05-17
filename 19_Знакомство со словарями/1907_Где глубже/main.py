d = {}
while True:
    s = input()
    if s == "":
        break
    name, depth = s.split()
    depth = int(depth)
    if name in d:
        d[name] = (min(d[name][0], depth), max(d[name][1], depth))
    else:
        d[name] = (depth, depth)
print(d)
