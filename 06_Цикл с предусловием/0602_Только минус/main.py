num = 0
count = 0

while num <= 36.6:
    num = input()
    if '_' in num:
        num = num.split('_')
        num = float(''.join(num))
    elif 'e' in num:
        num, e = num.split('e')
        num = float(num)
        e = int(e)
        num = num * 10 ** e
    else:
        num = float(num)

    if num < 0:
        count += 1

print(count)
