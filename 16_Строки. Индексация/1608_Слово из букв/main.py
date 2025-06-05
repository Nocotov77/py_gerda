n = int(input())
result = []
for i in range(1, n + 1):
    word = input().strip()
    if len(word) < i:
        print("None")
        exit()
    result.append(word[-i])
print(''.join(result))