import csv
import json

result = {"type": {}}
with open("catalog.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    for row in reader:
        t = row["type"]
        b = row["breed"]
        pet = {"name": row["name"], "age": row["age"], "gender": row["gender"], "owner": row["owner"],
               "phone": row["phone"]}
        if t not in result["type"]:
            result["type"][t] = {"breed": {}}
        if b not in result["type"][t]["breed"]:
            result["type"][t]["breed"][b] = []
        result["type"][t]["breed"][b].append(pet)
with open("pets.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)