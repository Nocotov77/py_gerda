## Задача: Замена символов в строке

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `input.txt`

**Вывод:** стандартный вывод или `output.txt`

### Описание

Напишите рекурсивную функцию `change(line, sub, symb)` для замены всех вхождений символа `sub` в строке `line` на символ `symb`.

**Важно:**

*   Метод `replace` использовать нельзя.
*   Использование рекурсии обязательно.

### Пример 1

**Ввод:**

```
text = "abracadabra"
print(change(text, "a", "o"))
```

**Вывод:**

```
obrocodobro
```

### Пример 2

**Ввод:**

```
text = "Fysh byte at bayt."
print(change(text, "y", "i"))
```

**Вывод:**

```
Fish bite at bait.
```