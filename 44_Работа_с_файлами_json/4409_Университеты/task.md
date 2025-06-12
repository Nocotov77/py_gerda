# Университеты

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** стандартный ввод или `state.txt`

**Вывод:** стандартный вывод или `state.json`

В файле `world_university_ranking.csv`, доступном вашему решению, записан рейтинг университетов мира с заголовками:

`rank,institution,location,ar score`

В текстовом файле `state.txt` записано название страны, для которой нужно получить список словарей с ключами: название университета (`institution`), рейтинг (`rank`), баллы рейтинга (`ar score`).

Полученный словарь запишите в файл `state.json`.

**Пример**

**Ввод**
```
Sudan
```

**Вывод**
```json
[
  {
    "institution": "University of Khartoum",
    "rank": "1380",
    "ar score": "5.8"
  },
  {
    "institution": "Sudan University of Science and Technology",
    "rank": "1410",
    "ar score": "3.3"
  }
]
```

**Примечания**

Первые несколько строк csv файла выглядят так:

```
rank,institution,location,ar score
1,Massachusetts Institute of Technology (MIT),United States,100
2,University of Cambridge,United Kingdom,100
3,Stanford University,United States,100
4,University of Oxford,United Kingdom,100
```

Весь файл можно скачать по ссылке.