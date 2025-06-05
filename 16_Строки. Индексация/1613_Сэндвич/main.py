s = input().strip()
length = len(s)
mid = (length + 1) // 2
result = []
for i in range(mid):
    result.append(s[i])
    if mid + i < length:
        result.append(s[mid + i])
print(''.join(result))