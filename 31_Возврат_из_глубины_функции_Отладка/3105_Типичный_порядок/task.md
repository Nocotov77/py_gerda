# Типичный порядок

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `input.txt`

**Вывод:** стандартный вывод или `output.txt`

Напишите функцию `positions()`, наводящую порядок в переменных.

Если аргумент функции – список, кортеж или множество, она возвращает наибольшее значение, если этот аргумент не пуст. Если пустой – вернуть `None`.

Если аргумент – число, то нужно вернуть следующее четное число.

Если строка – вернуть ее длину.

## Пример 1

**Ввод:**

```
print(positions(11.3))
```

**Вывод:**

```
12
```

## Пример 2

**Ввод:**

```
print(positions(42))
```

**Вывод:**

```
44
```

## Пример 3

**Ввод:**

```
print(positions((17, 2.5)))
```

**Вывод:**

```
17
```