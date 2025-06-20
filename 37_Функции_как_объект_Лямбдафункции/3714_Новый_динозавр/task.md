# Новый динозавр

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `input.txt`

**Вывод:** стандартный вывод или `output.txt`

Палеонтологи говорят, что нового динозавра или его части находят каждые 7 - 10 дней. Наверняка, не все из них принадлежат к новым видам. Обозначим динозавров двумя или тремя буквами латинского алфавита. Например, PD – PteroDactyl.

Напишите программу, которая из строки, в которой подстроки записаны через пробел, выберет только динозавров (2 или 3 символа), преобразует их в верхний регистр и запишет в словарь: ключ – динозавр, значение – сколько раз встречался в любом регистре.

При решении задачи используйте `filter`, `map`, `lambda`.

## Формат ввода

Вводится строка сокращений через пробел.

## Формат вывода

Выведите полученный словарь.

## Пример

**Ввод**
```
kS j TSR Hgy PsL Pw PW xOVn DD kS ACS j Hgy KS jaHc PD HgY TSR DD UAztj
```

**Вывод**
```
{'KS': 3, 'TSR': 2, 'HGY': 3, 'PSL': 1, 'PW': 2, 'DD': 2, 'ACS': 1, 'PD': 1}