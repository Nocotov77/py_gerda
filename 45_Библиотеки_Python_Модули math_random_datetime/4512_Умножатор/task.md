# Умножатор

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `input.txt`

**Вывод:** стандартный вывод или `output.txt`

Напишите функцию `multiplier()` для нахождения произведения элементов списка, подходящих под определенное условие.

Функция принимает произвольное количество позиционных аргументов-чисел и именованный аргумент `key`, получающий функцию для отбора чисел.

Функция возвращает произведение, если есть хоть один подходящий аргумент, или `None`, если таких аргументов не нашлось.

Используйте `math.prod()`

**Пример**

| Ввод                                                   | Вывод |
| ------------------------------------------------------ | ----- |
| `print(multiplier(2, 3, 4, 5, key=lambda x: x % 2))` | `15`  |