# Ожидание

- **Ограничение времени:** 1 секунда
- **Ограничение памяти:** 64Mb
- **Ввод:** стандартный ввод или `input.txt`
- **Вывод:** стандартный вывод или `output.txt`

Ждать и догонять всегда не очень приятно. Напишите функцию `days_left()`, которая определит, сколько осталось дней от сегодняшнего дня до переданной даты.

Дата в функцию передается в виде строки из трех чисел, разделенных точками, – дня, месяца и года.

## Пример 1

**Ввод**
```
print(days_left('31.12.2022'))
```

**Вывод**
```
364
```

## Пример 2

**Ввод**
```
print(days_left('28.01.2022'))
```

**Вывод**
```
27
```

## Примечания

В примерах системная дата 1.1.2022.
В примерах показано, что вернет функция при таком вызове.
Используйте библиотеку `datetime`.