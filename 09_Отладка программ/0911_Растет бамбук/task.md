# Растет бамбук

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `input.txt`

**Вывод:** стандартный вывод или `output.txt`

Бамбук – это очень быстрорастущая трава, имеющая очень разветвленную корневую систему. Из корней может вырастать множество побегов, поэтому целый бамбуковый лес может быть одним и тем же растением.

У одного из видов бамбука обнаружилась интересная закономерность скорости роста побегов от расстояния этого побега от основного растения, пустившего корни: каждая единица расстояния от основного ствола уменьшает скорость роста на 2% (от скорости роста основного растения), но только до половины скорости роста основного побега, дальше не уменьшается.

Напишите программу, которая выведет, на сколько вырастет побег на заданном расстоянии от основного за сутки.

## Формат ввода

Вводится скорость роста основного побега в мм в сутки. Затем вводится расстояние от основного побега до искомого в единицах расстояния.

## Формат вывода

Выведите, на сколько мм вырастет этот побег за сутки. Округлять не нужно.

## Пример 1

**Ввод**
```
100
22
```

**Вывод**
```
56.0
```

## Пример 2

**Ввод**
```
100
0
```

**Вывод**
```
100.0
```

## Пример 3

**Ввод**
```
100
30
```

**Вывод**
```
50.0
```

## Примечания

Допустим, скорость роста основного ствола 100 единиц. Тогда на расстоянии 1 скорость роста 100 - (100 * 0.02) = 98. На расстоянии 22: 100 - (100 * 0.02 * 22) = 56.