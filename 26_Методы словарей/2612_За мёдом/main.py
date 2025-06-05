d = {}
while True:
    s = input()
    if s == "":
        break
    name, equip = s.split(" - ", 1)
    d.setdefault(name, {}).setdefault(equip, 0)
    d[name][equip] += 1
for name, items in d.items():
    line = []
    for equip, count in items.items():
        line.append(f"{equip} ({count})")
    print(f"{name}: " + ", ".join(line))
