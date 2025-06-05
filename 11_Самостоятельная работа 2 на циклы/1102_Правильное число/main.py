wordslen = []

for i in range(3):
    wordslen.append(len(input()))

mid = 1

for i in range(3):
    if min(wordslen) <= wordslen[i] <= max(wordslen):
        mid = wordslen[i]
        break
    if min(wordslen) == wordslen[i] and wordslen[i] == max(wordslen):
        mid = wordslen[i]

step = min(wordslen) * -1
total = max(wordslen)

for i in range(max(wordslen), mid, step):
    print(total, end=' ')
    total += step
    