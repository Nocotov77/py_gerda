s = input().strip()
result = []
bracket_level = 0

for char in s:
    if char == '[':
        bracket_level += 1
    elif char == ']' and bracket_level > 0:
        bracket_level -= 1
    elif bracket_level == 0:
        result.append(char)

print(''.join(result))