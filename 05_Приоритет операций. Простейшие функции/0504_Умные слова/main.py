a, b, c = input(), input(), input()

if a > c:
    a, c = c, a
if b > c:
    c, b = b, c
if a > b:
    a, b = b, a

print(a, c, len(b), sep='\n')