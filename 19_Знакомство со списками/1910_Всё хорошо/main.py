lines = []
while True:
    line = input().strip()
    if not line:
        break
    lines.append(line)

indices = []
for idx, line in enumerate(lines):
    if "Все хорошо" in line:
        indices.append(idx)

start, end = indices[0], indices[1]

result = lines[start + 1: end]

for line in reversed(result):
    print(line)