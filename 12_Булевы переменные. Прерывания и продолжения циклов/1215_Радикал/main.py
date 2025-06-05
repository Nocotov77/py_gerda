n = int(input())
answer = []
d = 2
while d * d <= n:
    if n % d == 0:
        answer.append(d)
        n //= d
    else:
        d += 1
if n > 1:
    answer.append(n)
answer = set(answer)
result = 1
for i in answer:
    result *= i
print(result)