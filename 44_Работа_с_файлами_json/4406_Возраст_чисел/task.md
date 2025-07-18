# Возраст чисел

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод

**Вывод:** numbers_age.json

Математик Нил Слоун предложил измерять возраст чисел количеством шагов, которые потребуются чтобы из многозначного числа получить однозначное, используя операцию перемножения всех его знаков. Например, возьмём число 1792. Перемножим все его цифры, получим

1 * 7 * 9 * 2 = 126

1 * 2 * 6 = 12

1 * 2 = 2

Понадобилось три шага, значит, возраст этого числа – 3.

Основным ограничивающим продолжительность жизни барьером является ноль. Нил перебрал ВСЕ числа вплоть до 10 в степени 223 и не обнаружил ни одного числа с продолжительностью жизни больше 11!

Напишите программу, которая все вводимые числа будет записывать в словарь, ключом которого является возраст числа, а значением список чисел с таким возрастом.

Полученный словарь запишите в файл numbers_age.json.

## Формат ввода

Вводятся целые числа.

## Формат вывода

Ничего не выводится в консоль, полученный словарь записывается в файл.

## Пример

**Ввод**
```
1236598
9898989889
23654895
2365482
11111111225
326411588412
111111111113
```

**Вывод**
```json
{
  "2": [
    "1236598",
    "23654895",
    "2365482",
    "11111111225",
    "326411588412"
  ],
  "4": [
    "9898989889"
  ],
  "1": [
    "111111111113"
  ]
}
```

## Примечания

Если число сразу однозначное, то его возраст считается равным 1.