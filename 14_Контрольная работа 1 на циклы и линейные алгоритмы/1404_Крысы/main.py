s = ' '
words = []
n = int(input())
test = input()
counter = 0
k = 0

while s != 'КРЫСЫ':
    s = input()
    if s == 'КРЫСЫ':
        break
    if ('3' in s) or ('7' in s) or ('9' in s):
        continue
    if test not in s:
        counter += 1
    words.append(s)
    k += 1

words.sort(reverse=True)
for i in range(k):
    if len(words[i]) % n != 0:
        start = len(words[i])
        break

for i in range(start, counter, -1 * n):
    print(i, end=' ')