import csv

with open("alpha_oriona.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    next(reader)
    rows = list(reader)
if not rows:
    best_length = 0
    best_date = ""
    best_time = ""
else:
    best_length = 1
    best_date = rows[0][0]
    best_time = rows[0][1]
    curr_length = 1
    curr_date = rows[0][0]
    curr_time = rows[0][1]
    curr_val = float(rows[0][2])
    for row in rows[1:]:
        val = float(row[2])
        if val <= curr_val:
            curr_length += 1
        else:
            if curr_length > best_length:
                best_length = curr_length
                best_date = curr_date
                best_time = curr_time
            curr_length = 1
            curr_date = row[0]
            curr_time = row[1]
        curr_val = val
    if curr_length > best_length:
        best_length = curr_length
        best_date = curr_date
        best_time = curr_time
with open("result.txt", "w", encoding="utf-8") as f:
    f.write(str(best_length) + "\n")
    f.write(best_date + " " + best_time)