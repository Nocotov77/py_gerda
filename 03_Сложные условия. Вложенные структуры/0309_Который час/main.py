hour = input()
match hour:
    case '5' | '6' | '7' | '8' | '9' | '10':
        print('Утро')
    case '11' | '12' | '13' | '14' | '15' | '16' | '17':
        print('День')
    case '18' | '19' | '20' | '21' | '22':
        print('Вечер')
    case '23' | '0' | '1' | '2' | '3' | '4':
        print('Ночь')
    case _:
        print('Ошибка')