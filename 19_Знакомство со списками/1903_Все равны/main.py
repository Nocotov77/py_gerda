lines = []
while True:
    line = input().strip()
    if not line:
        break
    lines.append(line)

if not lines:
    print()
else:
    max_len = max(len(line) for line in lines)
    for line in reversed(lines):
        padding = max_len - len(line)
        left = padding // 2
        right = padding - left
        print('-' * left + line + '-' * right)