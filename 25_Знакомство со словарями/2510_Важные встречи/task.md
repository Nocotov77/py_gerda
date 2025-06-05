# Важные встречи

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `input.txt`

**Вывод:** стандартный вывод или `output.txt`

У Мефодия много важных встреч, многие планируются очень заранее. Напишите программу, которая поможет Мефодию ничего не забыть и не перепутать.

## Формат ввода

Вводится количество встреч, затем сами встречи в формате: название (или имя), день, месяц (через запятую и пробел)

Затем вводится месяц, для которого нужно выбрать встречи.

## Формат вывода

Выведите все встречи, назначенные на этот месяц, в порядке увеличения даты, в случае одинаковой – в алфавитном порядке.

## Пример 1

**Ввод**
```
7
Discussion, 4, May
Business Breakfast, 25, May
Viewing, 19, September
Meeting, 14, November
Delegation, 28, April
Session, 24, May
Conference, 28, November
May
```

**Вывод**
```
Discussion
Session
Business Breakfast
```

## Пример 2

**Ввод**
```
6
Report, 22, February
Session, 26, September
Conference, 22, February
Report, 25, December
Brainstorming, 8, February
Meeting, 6, November
February
```

**Вывод**
```
Brainstorming
Conference
Report