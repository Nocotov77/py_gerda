s1 = input().strip()
s2 = input().strip()
s3 = input().strip()

set1 = set(s1)
set2 = set(s2)
set3 = set(s3)

common_chars = []
for char in set1 | set2 | set3:
    count = 0
    if char in set1:
        count += 1
    if char in set2:
        count += 1
    if char in set3:
        count += 1
    if count >= 2:
        common_chars.append(char)

print(''.join(sorted(common_chars)))