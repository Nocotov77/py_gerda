a = input()
b = input()
c = input()

if a < b:
    a, b = b, a
if b < c:
    b, c = c, b
if a < b:
    a, b = b, a

print(a, b, c, sep=', ', end='.')