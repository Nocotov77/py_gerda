initial = int(input())
step = int(input())

current = initial
for _ in range(step - 1):
    num = current
    if num == 0:
        bin_current = '0'
    else:
        bin_current = []
        while num > 0:
            bin_current.append(str(num % 2))
            num = num // 2
        bin_current = ''.join(reversed(bin_current))

    ones = 0
    for c in bin_current:
        if c == '1':
            ones += 1

    num = ones
    if num == 0:
        bin_ones = '0'
    else:
        bin_ones = []
        while num > 0:
            bin_ones.append(str(num % 2))
            num = num // 2
        bin_ones = ''.join(reversed(bin_ones))

    new_bin = bin_current + bin_ones

    dec = 0
    power = 1
    for c in reversed(new_bin):
        if c == '1':
            dec += power
        power *= 2

    current = dec

print(current)