b = int(input())
c = int(input())
d = int(input())
merg = int(str(d) + str(c))
a = d + c * b

print(merg)
if a < merg:
    print('ДА')
else:
    print('НЕТ')