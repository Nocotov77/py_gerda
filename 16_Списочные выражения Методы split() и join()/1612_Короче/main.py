s = input().strip()
result = [s[i: len(s) - i] for i in range((len(s) + 1) // 2)]
print('\n'.join(result))