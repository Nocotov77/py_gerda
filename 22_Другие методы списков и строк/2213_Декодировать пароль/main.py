s = input().strip()
if not s:
    print('')
    exit()

groups = []
prev = s[0]
cnt = 1
for ch in s[1:]:
    if ch == prev:
        cnt += 1
    else:
        groups.append((prev, cnt))
        prev = ch
        cnt = 1
groups.append((prev, cnt))

result = []
i = 0
while i < len(groups):
    char, count = groups[i]
    if char != '%':
        if count >= 2:
            result.append(char)
            i += 1
        else:
            if i + 1 < len(groups) and groups[i + 1][0] == '%' and groups[i + 1][1] >= 2:
                result.append(char)
                i += 2
            else:
                i += 1
    else:
        i += 1

print(''.join(result))
