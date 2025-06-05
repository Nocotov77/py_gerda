s = input()
s1 = input()
s2 = input()
s3 = input()

proiz = 1

if s1 not in s and s2 not in s and s3 not in s:
    print('0')
    exit()

if s1 in s:
    proiz *= len(s1)
if s2 in s:
    proiz *= len(s2)
if s3 in s:
    proiz *= len(s3)

proiz *= 3

print(proiz / len(s))
