import re

n = int(input())
lines = [input().strip() for _ in range(n)]
k = int(input())
names = [input().strip() for _ in range(k)]

name_dict = {name: -1 for name in names}

for line_num, line in enumerate(lines, 1):
    words = line.split()
    for word in words:
        cleaned = re.sub(r'^[^a-zA-Z]+', '', word)
        cleaned = re.sub(r'[^a-zA-Z]+$', '', cleaned)
        parts = re.findall(r'[A-Za-z]+', cleaned)
        for part in parts:
            if part in name_dict and name_dict[part] == -1:
                name_dict[part] = line_num

for name in names:
    print(name_dict[name])