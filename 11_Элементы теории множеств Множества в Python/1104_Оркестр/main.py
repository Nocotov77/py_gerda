def read_instrument():
    names = set()
    while True:
        line = input().strip()
        if not line:
            break
        names.add(line)
    return names


goboe = read_instrument()
fleita = read_instrument()
saksofon = read_instrument()

all_names = goboe | fleita | saksofon

result = []
for name in all_names:
    count = 0
    if name in goboe:
        count += 1
    if name in fleita:
        count += 1
    if name in saksofon:
        count += 1
    if count == 1:
        result.append(name)

for name in sorted(result):
    print(name)