def white_combination(lst):
    keys = (-3, -2, -1, 1, 2, 3)
    counts = {k: 0 for k in keys}
    for x in lst:
        counts[x] += 1
    groups = [{1: 1, 2: 1, 3: 1}, {-1: 1, -2: 1, -3: 1}, {1: 1, -1: 1}, {2: 1, -2: 1}, {3: 1, -3: 1}]
    
    def can_part(c):
        if all(map(lambda k: c[k] == 0, c)):
            return True
        first = next(filter(lambda k: c[k] > 0, keys))
        for group in groups:
            if group.get(first, 0) and all(map(lambda k: c.get(k, 0) >= group.get(k, 0), group)):
                newc = {k: c[k] - group.get(k, 0) for k in c}
                if can_part(newc):
                    return True
        return False
    return can_part(counts)


lines = []
while True:
    try:
        s = input()
    except EOFError:
        break
    if s == "":
        break
    lines.append(s)
indexed_lines = list(enumerate(lines))
filtered_lines = list(filter(lambda x: white_combination(list(map(int, x[1].split()))), indexed_lines))
sorted_lines = sorted(filtered_lines, key=lambda x: (len(x[1].split()), x[0]))
for _, line in sorted_lines:
    print(line)