# Скобки-2

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `input.txt`

**Вывод:** стандартный вывод или `output.txt`

Напишите функцию `brackets()` для проверки правильности расстановки скобок четырех видов:

*   `[`
*   `]`
*   `(`
*   `)`
*   `{`
*   `}`
*   `<`
*   `>`

Функция возвращает `True`, если скобки расставлены правильно, и `False`, если неправильно.

## Пример 1

**Ввод**
```
line = "[12 / (9) + 2(5{15 * <2 - 3>}6)]"
print(brackets(line))
```

**Вывод**
```
True
```

## Пример 2

**Ввод**
```
line = "1{2 + [3}45 - 6] * (7 - 8) 9"
print(brackets(line))
```

**Вывод**
```
False
```

**Примечания**

Под правильностью расстановки скобок подразумевается, что каждая открывающая скобка имеет закрывающую, расположенную после нее и не перекрываемую другими открытыми скобками, а не правильность относительно чисел и знаков арифметических операций.

Например, `([{}])()<{}>` – правильное расположение скобок, а `({])` – неправильное.