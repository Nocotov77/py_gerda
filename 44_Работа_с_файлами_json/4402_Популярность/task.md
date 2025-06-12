# Популярность

*   Ограничение времени: 1 секунда
*   Ограничение памяти: 64Mb
*   Ввод: стандартный ввод или input.txt
*   Вывод: стандартный вывод или output.txt

Напишите программу, которая умеет выбирать информацию из файла json по запросу.

В исходном файле записан список словарей, в котором есть обязательные ключи (имя блогера, количество подписчиков, жанр, год, рейтинг), и необязательные, которые могут быть, а могут не быть.

## Формат ввода

В консоль вводится имя файла со списком словарей и запрос: по какому признаку создать словарь. Возможные варианты: жанр (category), год (started).

## Формат вывода

Создайте словарь с ключами – всеми возможными значениями по введенному запросу, и значениями – списками имен блогеров по этому ключу.

Выведите полученный словарь.

## Пример 1

**Ввод**

```
popularity.json
category
```

**Вывод**

```
{'Sports': ['WWE', 'Dude Perfect', 'Sports'], 'Gaming': ['PewDiePie', 'Fernanfloo']}
```

## Пример 2

**Ввод**

```
popularity.json
started
```

**Вывод**

```
{'2007': ['WWE', 'Dude Perfect'], '2011': ['PewDiePie', 'Fernanfloo'], '2013': ['Sports']}
```

## Примечания

Содержимое файла, который используется в примерах:

```json
[  
   {  
       "rank": "11",  
       "youtuber": "WWE",  
       "subscribers": "87600000",  
       "video views": "67,960,479,071",  
       "category": "Sports",  
       "started": "2007"  
   },  
   {  
       "rank": "6",  
       "youtuber": "PewDiePie",  
       "subscribers": "111000000",  
       "video views": "28,260,779,633",  
       "video count": "4472",  
       "category": "Gaming",  
       "started": "2011"  
   },  
   {  
       "rank": "46",  
       "youtuber": "Fernanfloo",  
       "subscribers": "44800000",  
       "video views": "9,834,587,080",  
       "video count": "541",  
       "category": "Gaming",  
       "started": "2011"  
   },  
   {  
       "rank": "25",  
       "youtuber": "Dude Perfect",  
       "subscribers": "57400000",  
       "video views": "14,219,518,587",  
       "video count": "287",  
       "category": "Sports",  
       "started": "2007"  
   },  
   {  
       "rank": "15",  
       "youtuber": "Sports",  
       "subscribers": "75100000",  
       "video views": "22,156,639,371",  
       "category": "Sports",  
       "started": "2013"  
   }  
]