## Пробежка

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `input.txt`

**Вывод:** стандартный вывод или `output.txt`

Все знают, как важно поддерживать себя в хорошей спортивной форме. Вот и По считает, что просто так бежать по кругу скучно и не полезно для здоровья. Нужно сначала запланировать себе тренировку, рассчитать дистанцию, сколько будет сожжено калорий, какой может быть пульс и кровяное давление…

Но нет, все равно пора бежать, не отвертишься, По!

Напишите функцию, которая всё посчитает, а По пусть бежит!

Функция `jogging()` принимает один позиционный и 3 именованных аргумента:

*   длительность тренировки (минут);
*   `speed` − средняя скорость бега (метров в секунду);
*   `kkal` − количество сжигаемых килокалорий за каждый километр бега;
*   `reduce` − сколько нужно сжечь килокалорий в результате тренировки.

Функция возвращает реальное количество сожжённых килокалорий, если считать, что они сжигаются только за полный километр, неполные не считаются, и достигнут ли результат.

**Пример 1**

**Ввод**

```
workout_time = 90
print(jogging(workout_time, speed=2,
              reduce=1000,
              kkal=100))
```

**Вывод**

```
(1000, True)
```

**Пример 2**

**Ввод**

```
workout_time = 15
print(jogging(workout_time, speed=2,
              reduce=800,
              kkal=80))
```

**Вывод**

```
(80, False)
```

**Примечания**

В тестирующую систему сдайте только функцию, но не код, её вызывающий.