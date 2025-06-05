# Итого

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или input.txt

**Вывод:** стандартный вывод или output.txt

Напишите функцию `total()` для подсчета общей калорийности заказанных блюд. В качестве аргумента в функцию передается список строк: блюдо и его калорийность через пробел. После каждого вызова калорийность суммируется и выводится общий итог в виде (блюда отсортированы в алфавитном порядке):

`<Блюдо> - <количество порций> - <калорийность всех порций, точность до десятых> kCal`  
`...`  
`------`  
`Total: <общая калорийность с точностью до 1 знака после запятой> kCal`

В конце – пустая строка для разделения вызовов функции.

## Пример

**Ввод**
```
data = ["Ice cream, strawberry 192",
        "Puff pastry with protein cream 461"]
total(data)
data = ["Orange juice drink 54.5",
        "Ice cream, strawberry 192",
        "Puff pastry with protein cream 461"]
total(data)
```

**Вывод**
```
Ice cream, strawberry - 1 - 192.0 kCal
Puff pastry with protein cream - 1 - 461.0 kCal
------
Total: 653.0 kCal

Ice cream, strawberry - 2 - 384.0 kCal
Orange juice drink - 1 - 54.5 kCal
Puff pastry with protein cream - 2 - 922.0 kCal
------
Total: 1360.5 kCal