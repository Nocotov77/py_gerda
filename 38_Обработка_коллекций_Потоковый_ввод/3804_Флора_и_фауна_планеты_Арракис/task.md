# Флора и фауна планеты Арракис

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод

**Вывод:** стандартный вывод или output.txt

Природа на планете Арракис, или планете Дюна, не отличается разнообразием, уж больно жестокие условия жизни, чрезвычайно низкая влажность и практически сплошная пустыня. Но даже здесь развились уникальные формы, а некоторые были завезены с других планет и адаптировались. Теперь уже можно приступать к систематическому описанию.

Напишите программу, которая из введённых строк составит энциклопедию биоформ по месту обитания. Поскольку жизненные формы немногочисленны, то их всех будем заносить в один список.

## Формат ввода

Вводятся строки вида

`жизненная форма // место обитания // тип`

В последней строке вводится название местности.

## Формат вывода

Для указанной местности надо записать всех обитателей в формате:

`жизненная форма (тип);`

а затем вывести в обратном алфавитном порядке, каждую с новой строки.

## Пример 1

**Ввод**
```
saguaro // Arrakeen // plant
donkey Bush // Carthage // plant
saguaro // Drum Sands // plant
fox-fennec fox // Arrakeen // animal
creosote shrub // Harg Pass // plant
asinine bush // Arrakeen // plant
creosote shrub // Drum Sands // plant
kangaroo mouse // Arrakeen // animal
Arrakeen
```

**Вывод**
```
saguaro (plant);
kangaroo mouse (animal);
fox-fennec fox (animal);
asinine bush (plant);
```

## Пример 2

**Ввод**
```
melon tree // Great Bled // plant
fungus-scavenger // Border of the Worm // mushroom
sand verbena // Great Bled // plant
desert hawk // Great Bled // animal
barrel cactus // Great Bled // plant
tumbleweed // Great Bled // plant
dragon root // Border of the Worm // the plant
Great Bled
```

**Вывод**
```
tumbleweed (plant);
sand verbena (plant);
melon tree (plant);
desert hawk (animal);
barrel cactus (plant);
```

## Примечания

Жизненные формы одной местности не повторяются.