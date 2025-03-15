str1 = input()
str2 = input()

if (str1 == 'Быть' and str2 == 'Быть') or (str1 == 'Не быть' and str2 == 'Не быть'):
    print('Выбор сделан!')
elif (str1 == 'Быть' and str2 == 'Не быть') or (str1 == 'Не быть' and str2 == 'Быть'):
    print('Вот в чём вопрос!')
else:
    print('Определитесь!')