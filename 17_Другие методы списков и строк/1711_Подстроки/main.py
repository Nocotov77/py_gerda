s = input().strip()
n = len(s)
max_len = n // 2
substrings = {}

for i in range(n):
    for length in range(1, max_len + 1):
        if i + length > n:
            break
        substr = s[i:i+length]
        substrings[substr] = substrings.get(substr, 0) + 1

result = {k: v for k, v in substrings.items() if v > 1}

for key in sorted(result.keys()):
    print(f"{key}: {result[key]}")