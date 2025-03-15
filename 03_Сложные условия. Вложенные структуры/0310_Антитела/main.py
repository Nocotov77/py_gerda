s1 = input()
s2 = input()
s3 = input()

if (s1 > s3):
    s1, s3 = s3, s1

if (s1 > s2):
    s1, s2 = s2, s1

if (s2, s3):
    s2, s3 = s3, s2

b = False

if (len(s1) == 5 and '0' in s1):
    print(s1, end='')
    b = True

if (len(s2) == 5 and '0' in s2):
    if (b):
        print(', ' + s2, end='')
    else:
        print(s2, end='')
    b = True

if (len(s3) == 5 and '0' in s3):
    if (b):
        print(', ' + s3, end='')
    else:
        print(s3, end='')