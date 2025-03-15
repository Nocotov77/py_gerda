import sys

# Ввод данных
s1 = input()
s2 = input()
s3 = input()
s4 = input()
space = False

# Проверка наличия хотя бы одного цветка в букете
if s1 in s4 or s2 in s4 or s3 in s4:
    print("В букете есть ", end="")
else:
    print("Таких цветов в букете нет.")
    sys.exit()

# Вывод цветов с правильным форматированием
if s1 in s4:
    print(s1, end="")
    space = True

if s2 in s4:
    if space:
        print(", " + s2, end="")
    else:
        print(s2, end="")
    space = True

if s3 in s4:
    if space:
        print(", " + s3, end="")
    else:
        print(s3, end="")
    space = True

print(".")