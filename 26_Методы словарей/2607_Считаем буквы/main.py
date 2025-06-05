import string
s = input()
d = {c: 0 for c in string.ascii_uppercase}
for c in s:
    if c.isalpha():
        d[c.upper()] += 1
print(d)
