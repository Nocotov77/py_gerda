import sys
import math

lines = sys.stdin.read().splitlines()
nums = []
for line in lines:
    if line.strip() == "": 
        continue
    n = int(line.strip())
    if n == 0: 
        break
    nums.append(n)

    
def dcount(n):
    cnt, i = 0, 1
    while i * i <= n:
        if n % i == 0:
            cnt += 1 if i * i == n else 2
        i += 1
    return cnt

    
res = [(x, dcount(x)) for x in nums]
res.sort(key=lambda t: (t[1], t[0]))
print(res)