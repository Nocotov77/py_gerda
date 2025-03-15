s1 = input()

if ('*' in s1 or '?' in s1) and ' ' not in s1:
    print('Возможно маска')
else:
    print('Нет, это не маска!')