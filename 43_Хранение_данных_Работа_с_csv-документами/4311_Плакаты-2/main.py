import csv


def sort_key(row):
    return tuple(int(row[idx[k]]) if k in num_fields else row[idx[k]] for k in keys)


with open("in_file.txt", "r", encoding="utf-8") as f:
    keys = [line.strip() for line in f.read().splitlines() if line.strip()]
num_fields = {"id", "h_dimension", "v_dimension", "price"}
with open("posters.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    header = next(reader)
    idx = {h: i for i, h in enumerate(header)}
    rows = list(reader)
rows.sort(key=sort_key)
with open("sorted.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerows(rows)