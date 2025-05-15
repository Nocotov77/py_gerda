s = input().strip()
hyphen_pos = -1
for i in range(len(s)):
    if s[i] == '-':
        hyphen_pos = i
        break
print(s[hyphen_pos + 1:] + '-' + s[:hyphen_pos])