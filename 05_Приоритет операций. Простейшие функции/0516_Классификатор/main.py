s1 = input()
s2 = input()
s3 = input()

if len(s1) <= len(s2) and len(s1) <= len(s3):
    if len(s2) <= len(s3):
        first = s1
        second = s2
        third = s3
    elif len(s3) < len(s2):
        first = s1
        second = s3
        third = s2
elif len(s2) <= len(s1) and len(s2) <= len(s3):
    if len(s1) <= len(s3):
        first = s2
        second = s1
        third = s3
    elif len(s3) < len(s1):
        first = s2
        second = s3
        third = s1
else:
    if len(s1) <= len(s2):
        first = s3
        second = s1
        third = s2
    elif len(s2) < len(s1):
        first = s3
        second = s2
        third = s1

if len(first) == len(second) and first > second:
    first, second = second, first
if len(second) == len(third) and second > third:
    second, third = third, second
if len(first) == len(second) and first > second:
    first, second = second, first

print(first, second, third, sep='\n')
