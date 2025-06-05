# Не продешевить

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `run.py`

**Вывод:** стандартный вывод или `output.txt`

Вот это удача! Нильс быстро схватил сачок и через мгновение гном уже барахтался в сетке, как пойманная стрекоза.

– Отпусти меня, Нильс, я дам тебе большую золотую монету, – взмолился гном.

Тут Нильсу пришло в голову, что хорошо бы не продешевить. Вдобавок к золотой монете можно ведь потребовать, чтобы гном учил за него уроки. Да мало ли что ещё можно придумать! Гном теперь на всё согласится! Когда сидишь в сачке, торговаться не станешь.

И Нильс снова тряхнул сеткой.

Напишите функцию `get_expensive()`, которая из всех предложений гнома (аргументов-строк при различных вызовах функции) выберет самое длинное, если в нем есть слово `гном` (`gnome`) в любой форме и в любом регистре.

В этом случае функция возвращает самую длинную из строк.

Если слова `гном` нет, то нужно вернуть:

`What do you offer for freedom, gnome?`

## Пример 1

**Ввод:**

```python
data = ('It would be good not to sell out.', 'for a gnome to learn his lessons for him', 'Gnome offered a coin', 'The gnome will agree to everything now!')
for item in data:
    print(get_expensive(item))
```

**Вывод:**

```
What do you offer for freedom, gnome?
for a gnome to learn his lessons for him
for a gnome to learn his lessons for him
for a gnome to learn his lessons for him
```

## Пример 2

**Ввод:**

```python
data = ('To ask?', 'Gnome, can you give me a slingshot?', 'I wish the gnome would give me a lot of money!', "I don't know what else to ask!")
for item in data:
    print(get_expensive(item))
```

**Вывод:**

```
What do you offer for freedom, gnome?
Gnome, can you give me a slingshot?
I wish the gnome would give me a lot of money!
What do you offer for freedom, gnome?