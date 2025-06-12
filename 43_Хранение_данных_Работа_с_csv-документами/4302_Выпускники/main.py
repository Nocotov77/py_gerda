import csv

threshold = int(input().strip())
with open("vps.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    next(reader)
    for row in reader:
        if int(row[4].strip()) >= threshold:
            print(row[0].strip())