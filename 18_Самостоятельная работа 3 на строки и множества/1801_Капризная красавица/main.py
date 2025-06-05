n = int(input())
s = ""
set1 = {n}

while True:
    n = int(input())
    if n % 10 == 0:
        break
    set1.add(n)

n = int(input())
set2 = {n}

while True:
    n = int(input())
    if n % 10 == 0:
        break
    set2.add(n)

diff = set2 - set1

list1 = []
list1.extend(diff)
k = len(list1)

for i in range(k):
    if list1[i] % 2 != 0:
        s += str(list1[i]) + "#"

print(s)