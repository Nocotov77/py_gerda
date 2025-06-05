d = {
    "Cenozoic": (0, 145000),
    "Mesozoic": (145000, 300000),
    "Paleozoic": (300000, 635000),
    "Proterozoic": (635000, 2800000),
    "Archaea": (2800000, 4500001)
}
while True:
    s = input()
    if s == "":
        break
    n = int(s)
    for k, (lo, hi) in sorted(d.items(), key=lambda x: x[1][0]):
        if lo <= n < hi:
            print(k)
            break
