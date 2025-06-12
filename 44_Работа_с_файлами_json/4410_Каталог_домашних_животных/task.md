# Каталог домашних животных

**Ограничение времени:** 1 секунда

**Ограничение памяти:** 64Mb

**Ввод:** `catalog.csv`

**Вывод:** `pets.json`

Все любят кошек и собак. Если их много, это прекрасно, но нужно упорядочить информацию о них и об их хозяевах.

В файле `catalog.csv` находится информация о домашних животных в формате:

`вид животного; порода; кличка; возраст; пол; фамилия и инициалы хозяина; телефон хозяина.`

Нужно из этих данных составить каталог по видам животных. Это словарь, в котором есть ключ `type` – вид животных, его значение – список словарей с информацией о каждом виде животных, каждый вид также содержит список словарей уже о каждом конкретном животном. Полученный словарь запишите в файл `pets.json`.

Чтобы было понятней, смотрите пример входного и выходного файлов.

## Пример

**Ввод**

```
type;breed;name;age;gender;owner;phone
cat;siamese;Barsik;15;male;Ivanov A.V.;+79160123456
cat;abyssinian;Asia;8;female;Sorokina T.V.;+79035620124
dog;british longhair;Tusik;3;male;Sidorov N.B.;+79853752145
cat; maine coon;Martin;1;male;Pushkin A.S.;+78523145698
cat;siamese;Mursik;5;male;Ivanov A.V.;+79160123456
dog;york;Sonya;4;female;Dobrov F.P.;+76549592321
```

**Вывод**

```json
{
  "type": {
    "cat": {
      "breed": {
        "siamese": [
          {
            "name": "Barsik",
            "age": "15",
            "gender": "male",
            "owner": "Ivanov A.V.",
            "phone": "+79160123456"
          },
          {
            "name": "Mursik",
            "age": "5",
            "gender": "male",
            "owner": "Ivanov A.V.",
            "phone": "+79160123456"
          }
        ],
        "abyssinian": [
          {
            "name": "Asia",
            "age": "8",
            "gender": "female",
            "owner": "Sorokina T.V.",
            "phone": "+79035620124"
          }
        ],
        " maine coon": [
          {
            "name": "Martin",
            "age": "1",
            "gender": "male",
            "owner": "Pushkin A.S.",
            "phone": "+78523145698"
          }
        ]
      }
    },
    "dog": {
      "breed": {
        "british longhair": [
          {
            "name": "Tusik",
            "age": "3",
            "gender": "male",
            "owner": "Sidorov N.B.",
            "phone": "+79853752145"
          }
        ],
        "york": [
          {
            "name": "Sonya",
            "age": "4",
            "gender": "female",
            "owner": "Dobrov F.P.",
            "phone": "+76549592321"
          }
        ]
      }
    }
  }
}
```

**Примечания**

Ничего не вводится с клавиатуры, ничего не выводится в консоль, все действия производятся с файлами.