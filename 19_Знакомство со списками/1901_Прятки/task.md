# Прятки

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `input.txt`

**Вывод:** стандартный вывод или `output.txt`

Раз, два, три, четыре, пять, я иду искать!

Найдите всех спрятавшихся детей. Или хотя бы кого-то.

## Формат ввода

Вводится количество играющих, затем строки, в которых могут быть их имена. Затем вводится количество имен и сами имена детей для поиска.

## Формат вывода

Для каждого имени выведите номер строки (счет с 1), в которой оно первый раз встретилось, или -1, если такого имени не было.

## Пример

**Ввод:**

```
7
Bessy kept the garden gate,
And Mary kept the pantry.
Little Betty Blue Lost her holiday shoe.
Billy, Billy, come and play.
Yes, my Polly, so I will.
Little Bobby Snooks was fond of his books.
Robert Barnes, my fellow fine, can you shoe this horse of mine?
4
Mary
Jack
Billy
Bobby
```

**Вывод:**

```
2
-1
4
6