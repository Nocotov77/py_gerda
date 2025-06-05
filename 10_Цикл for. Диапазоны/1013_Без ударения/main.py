c = 0
total = 0
s = input()
line_len = 0

for i in s:
    line_len += 1
    if (i == 'а' or i == 'я' or i == 'о' or i == 'ё' or i == 'э' or i == 'е' or i == 'у'
            or i == 'ю' or i == 'ы' or i == 'и'):
        c += 1
    if i == " " or line_len == len(s):
        if c != 0:
            total += c - 1
            c = 0


print(total)