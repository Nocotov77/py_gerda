s1 = input()
s2 = input()
S = 1
V = 1

if '_' in s1:
    s1 = s1.split('_')
    S = float(''.join(s1))
elif 'e' in s1:
    s1, e = s1.split('e')
    s1 = float(s1)
    e = int(e)
    S = s1 * 10 ** e
else:
    S = float(s1)

if '_' in s2:
    s2 = s2.split('_')
    V = float(''.join(s2))
elif 'e' in s2:
    s2, e = s2.split('e')
    s2 = float(s2)
    e = int(e)
    V = s2 * 10 ** e
else:
    V = float(s2)

T = S / V
T = T / 3600 / 24 / 365
print(T)