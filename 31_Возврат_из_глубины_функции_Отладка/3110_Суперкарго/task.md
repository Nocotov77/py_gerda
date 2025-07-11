# Суперкарго

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или input.txt

**Вывод:** стандартный вывод или output.txt

Итак, вы — суперкарго. Вам нужно разместить на судне переданный груз. Грузы будем обозначать целыми числами, а палуб на нашем судне три: на нижней размещаются только трёхзначные числа, на средней двузначные, на верхней однозначные. Никакие другие наш корабль взять не может.

Напишите функцию `supercargo(load, capacity)`, принимающую в качестве аргументов кортеж чисел-грузов и кортеж вместимостей палуб — сначала верхней, затем средней, потом нижней.

Функция возвращает кортеж нераспределённых грузов и логическое значение: удалось загрузить судно полностью или нет (то есть, если не осталось свободных мест ни на одной палубе, значит, удалось).

В качестве ответа сдайте только код, содержащий указанную функцию. Вызывать её не нужно!

## Пример 1

**Ввод**
```
loads_data = (23, 12, 1, 345, 123, 3, 9999)
capacity_data = (2, 1, 0)
res = supercargo(loads_data, capacity_data)
print(res[0], res[-1], sep="\n")
```

**Вывод**
```
(12, 345, 123, 9999)
True
```

## Пример 2

**Ввод**
```
loads_data = (23, 12, 1, 345, 123, 3)
capacity_data = (2, 2, 3)
res = supercargo(loads_data, capacity_data)
print(res[0], res[-1], sep="\n")
```

**Вывод**
```
()
False
```

## Примечания

Значения в кортеже могут быть записаны в любом порядке.