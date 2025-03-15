import sys
from math import floor

n1 = int(input())
n2 = int(input())

if n2 == 0:
    print('Не делится!')
    sys.exit()

print('Каждому по ' + str(floor(n1 / n2)))
print('Осталось ' + str(n1 - floor(n1 / n2) * n2))