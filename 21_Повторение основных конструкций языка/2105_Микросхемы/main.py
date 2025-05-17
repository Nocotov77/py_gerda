chips = {}
while True:
    line = input()
    if line == "":
        break
    parts = line.split()
    des = parts[0]
    base = int(parts[1])
    if len(parts) > 2:
        comps = parts[2].split(',')
        tot = base
        for c in comps:
            tot += chips[c]
    else:
        tot = base
    chips[des] = tot
print(max(chips.values()))
