import csv
import sys


def messier_search(param):
    values = set()
    with open("messier.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        header = next(reader)
        try:
            idx = header.index(param)
        except ValueError:
            return []
        for row in reader:
            if row[idx].strip():
                values.add(row[idx].strip())
    return sorted(values)