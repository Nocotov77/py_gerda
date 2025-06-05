words = []
n = int(input())
test1 = input()
test2 = 'забыл'
count = 0

for i in range(n):
    words.append(input())
    if test1 in words[i] or test2 in words[i]:
        count += 1

if count <= n / 2:
    print('НЕ ТАК И МНОГО')
else:
    print('ВСЕ РАВНО НИЧЕГО СТРАШНОГО')

print(count + n)