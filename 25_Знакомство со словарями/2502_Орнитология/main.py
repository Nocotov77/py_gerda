d = {}
while True:
    s = input()
    if s == "":
        break
    k, v = s.split(": ")
    d[k] = d.get(k, 0) + int(v)
print(d)
