# Принц и нищий

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `input.txt`

**Вывод:** стандартный вывод или `output.txt`

Принцу интересно, как живет его народ, а нищему хочется не заботиться, наконец, о самом насущном. Помогите им обменяться контентом.

Напишите функцию `change()`, которая меняет местами списки в переменных `prince` и `pauper`.

## Пример

**Ввод**
```
prince = [1, 2, 3]
pauper = ["one", "two", "three"]
old_prince = prince.copy()
old_pauper = pauper.copy()
change()
print(prince, old_pauper, prince == old_pauper)
print(pauper, old_prince, pauper == old_prince)
```

**Вывод**
```
['one', 'two', 'three'] ['one', 'two', 'three'] True
[1, 2, 3] [1, 2, 3] True
```

## Примечания

В задаче нельзя использовать инструкцию `global`.