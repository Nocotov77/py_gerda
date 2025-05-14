word = input().strip()
result = []
for i in range(len(word)):
    result.append(word[i] * (i + 1))
print(''.join(result))