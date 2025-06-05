result = []
while True:
    word = input().strip()
    if not word:
        break
    if len(word) == len(set(word)):
        result.append(word)
for w in result:
    print(w)