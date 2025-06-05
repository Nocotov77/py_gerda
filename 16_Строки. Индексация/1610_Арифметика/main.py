s = input().strip()
result = int(s[0])
for i in range(1, len(s), 2):
    operator = s[i]
    num = int(s[i+1])
    if operator == '+':
        result += num
    else:
        result -= num
print(result)