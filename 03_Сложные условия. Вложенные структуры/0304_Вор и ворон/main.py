str1 = input()

if 'ворон' not in str1 and (('вор' in str1) or ('Вор' in str1)):
    print('Полиция!')
elif 'ворон' in str1:
    print('Кар!')