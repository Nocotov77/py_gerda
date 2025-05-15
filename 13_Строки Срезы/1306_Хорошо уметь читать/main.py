s = input().strip()
familar = {'E', 'S', 'M'}

first_pos = 0
for i in range(len(s)):
    if s[i] in familar:
        first_pos = i + 1
        break

if first_pos == 0:
    part2 = len(s)
else:
    start_idx = first_pos - 1
    next_idx = -1
    for i in range(start_idx + 1, len(s)):
        if s[i] in familar:
            next_idx = i
            break
    part2 = (next_idx - start_idx - 1) if next_idx != -1 else (len(s) - start_idx - 1)

unknown = set()
for c in s:
    if c != ' ' and c not in familar:
        unknown.add(c)

print(first_pos)
print(part2)
print(len(unknown))