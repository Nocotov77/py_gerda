# На помощь

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод

**Вывод:** стандартный вывод

Недолго раздумывая, калиф ринулся туда, откуда слышались жалобные стоны.

Недаром визирь называл себя правой рукой калифа. И хотя теперь у калифа не было ни правой руки, ни левой, визирь не покинул своего господина и бросился за ним.

Напишите функцию `to_rescue()`, которая определит, что ждет их впереди.

В переменной `need_help` находится список строк для преобразования.

Функция принимает позиционный аргумент-строку и именованный параметр `additional` со значением по умолчанию `-`.

Для каждой строки из списка нужно найти буквы, которых нет в строке – аргументе функции (без повторений), расположить по алфавиту и, если длина полученной строки оказалась меньше длины строки-аргумента, дополнить в конце символами из аргумента `additional`.

Преобразованные строки записать на прежнее место в переменную `need_help`.

## Пример 1

**Ввод**
```python
need_help = ['tears', 'flowed', 'from', 'the', 'owls', 'yellow', 'eyes']
to_rescue('large', additional='*')
print(need_help)
```

**Вывод**
```
['st***', 'dfow*', 'fmo**', 'ht***', 'osw**', 'owy**', 'sy***']
```

## Пример 2

**Ввод**
```python
need_help = ['owl', 'was', 'crying', 'bitterly']
to_rescue('caliph')
print(need_help)
```

**Вывод**
```
['ow----', 'sw----', 'gnry--', 'berty-']