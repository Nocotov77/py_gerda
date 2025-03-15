import sys
from math import floor

s1 = input()
s2 = input()
n = int(input())

if (s1 == 'A' and s2 == 'B') or (s1 == 'B' and s2 == 'A'):
    print('NOT TO GO')
    sys.exit()
elif s1 == 'A' or s2 == 'A':
    n = floor((n - 5) / 2)
elif s1 == 'B' or s2 == 'B':
    n = floor((n - 3) / 2)
else:
    print('NOT TO GO')
    sys.exit()

print(n)