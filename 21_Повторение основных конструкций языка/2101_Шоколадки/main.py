n = int(input())
f = int(input())
v = n // 3
r = n - v
friends = r // f
vasya = v + r % f
print(vasya, friends)
