# Космический ветер

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или input.txt

**Вывод:** стандартный вывод или output.txt

Спутник, запущенный на околоземную орбиту, получает данные об энергии попавших в детектор космических частиц. Это могут быть частицы как земного (атмосферного) происхождения, так и солнечные или даже пришедшие из межзвездного пространства. Особый интерес представляют высокоэнергетические частицы, поскольку в космическом ветре можно встретить частицы таких энергий, которые пока недостижимы на наземных ускорителях, таких как БАК, например.

Все полученные данные нужно распределить по интервалам и вывести количество частиц, полученных в каждом интервале энергий, а также среднее значение энергии в каждом интервале.

## Формат ввода

Передается строка, содержащая данные в виде вещественных чисел, записанных через пробел.

## Формат вывода

Все данные нужно распределить по диапазонам: до 10; от 10 до 100; от 100 до 1000; свыше 1000.
Для каждого диапазона вывести через запятую количество частиц, попавших в диапазон и среднее значение энергии в этом диапазоне с точностью до 1 знака после запятой. Если в диапазоне нет частиц, он не выводится.

## Пример 1

**Ввод**
```
858.0 1290.3 1283.4 1844.2 1929.0 598.2 21.9 1995.6 1662.3 1493.7
```

**Вывод**
```
от 10 до 100: 1, 21.9
от 100 до 1000: 2, 728.1
свыше 1000: 7, 1642.6
```

## Пример 2

**Ввод**
```
455.7 1609.9 849.8 272.4 1338.5
```

**Вывод**
```
от 100 до 1000: 3, 526.0
свыше 1000: 2, 1474.2