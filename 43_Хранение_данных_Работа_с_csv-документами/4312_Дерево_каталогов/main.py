with open("in_file.csv", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()
parent_children = {}
parents = set()
children = set()
for line in lines:
    if line.strip():
        p, c = [x.strip() for x in line.split(";")]
        parents.add(p)
        children.add(c)
        parent_children.setdefault(p, []).append(c)
top = (parents - children).pop()
levels = []
current = [top]
while current:
    current_sorted = sorted(current)
    levels.append(current_sorted)
    next_level = []
    for node in current:
        if node in parent_children:
            next_level.extend(parent_children[node])
    current = next_level
with open("out_file.csv", "w", encoding="utf-8") as f:
    for level in levels:
        f.write(";".join(level) + "\n")