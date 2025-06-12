# Реестр драконов

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** `dragons.csv`

**Вывод:** `dragons.json`

В последнее время в Земноморье развелось что-то слишком много драконов. Кроме доморощенных, спокойных и прирученных, появились пришлые, агрессивные, все норовят богатыря съесть, его лошадью закусить. А то деревеньку ненароком сожгут, огнем из пасти попыхивая. Надо перепись драконов произвести, порядок чтоб был.

В файле `dragons.csv` составлен перечень драконов. Первая строка – заголовки, в остальных значения свойств для каждого из драконов.

Составьте словарь с ключом `dragons`, значение по этому ключу – список словарей, структура которых показана ниже.

```json
{
    "dragons": [
        {
            "place": "Havnor",
            "name": "Dragon_1",
            "nature": "nordic",
            "number_of_heads": "3",
            "possession_of_the_true_speech": "1"
        },
        {
            "place": "Hadzor", ...
        }, ...
    ]
}
```

В файл `dragons.json` запишите полученный словарь.

## Формат ввода

Ничего не вводится с клавиатуры.

## Формат вывода

Ничего не выводится в консоль. Все действия производятся с файлами. В примере показано их содержимое.

## Пример

**Ввод**

```
name,place,nature,number_of_heads,possession_of_the_true_speech
Tifon,Tehanu,nordic,3,0
Midgardsorm,Tehanu,introvert,5,1
Kalessin,Cargad,anxious,1,1
```

**Вывод**

```json
{
    "dragons": [
        {
            "name": "Tifon",
            "place": "Tehanu",
            "nature": "nordic",
            "number_of_heads": "3",
            "possession_of_the_true_speech": "0"
        },
        {
            "name": "Midgardsorm",
            "place": "Tehanu",
            "nature": "introvert",
            "number_of_heads": "5",
            "possession_of_the_true_speech": "1"
        },
        {
            "name": "Kalessin",
            "place": "Cargad",
            "nature": "anxious",
            "number_of_heads": "1",
            "possession_of_the_true_speech": "1"
        }
    ]
}