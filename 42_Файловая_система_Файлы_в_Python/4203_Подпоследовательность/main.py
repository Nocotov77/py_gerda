with open("sequence.txt", "r", encoding="utf-8") as f:
    s = f.read().strip()
if not s:
    print(0)
else:
    current = 1
    max_len = 1
    for i in range(1, len(s)):
        if s[i - 1] == 'D' and s[i] == 'F':
            current = 1
        else:
            current += 1
        if current > max_len:
            max_len = current
    print(max_len)