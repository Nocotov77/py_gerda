import csv

district = input().strip()
years = input().strip().split()
init_year, fin_year = years[0], years[1]
res = []
with open("salary.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    header = next(reader)
    init_index = header.index(init_year)
    fin_index = header.index(fin_year)
    for row in reader:
        if row[1].strip() == district:
            init_salary = int(row[init_index].replace(" ", ""))
            fin_salary = int(row[fin_index].replace(" ", ""))
            if fin_salary < init_salary * 1.04:
                res.append((row[0].strip(), row[init_index].strip(), row[fin_index].strip()))
with open("out_file.csv", "w", encoding="utf-8") as f:
    if res:
        f.write(f"Субъект;{init_year};{fin_year}\n")
        for r in res:
            f.write(";".join(r) + "\n")
    else:
        f.write("")