import csv

with open("in_file.txt", "r", encoding="utf-8") as f:
    sort_field = f.read().strip()
rows = []
with open("posters.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    header = next(reader)
    idx = header.index(sort_field)
    for row in reader:
        rows.append(row)
if sort_field in {"id", "h_dimension", "v_dimension", "price"}:
    rows.sort(key=lambda x: int(x[idx]))
else:
    rows.sort(key=lambda x: x[idx])
with open("sorted.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerows(rows)