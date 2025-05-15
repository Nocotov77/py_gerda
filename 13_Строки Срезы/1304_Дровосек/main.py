s = input().strip()
k = int(input())
result = []
cut_from_end = True

while len(s) > k:
    if cut_from_end:
        part = s[-k:]
        s = s[:-k]
    else:
        part = s[:k]
        s = s[k:]
    result.append(part)
    cut_from_end = not cut_from_end

if s:
    result.append(s)

print('\n'.join(result))