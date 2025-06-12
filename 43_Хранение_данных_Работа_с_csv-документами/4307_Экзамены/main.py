import sys
data = sys.stdin.read().splitlines()


if data:
    n, m = map(int, data[0].split())
    valid = []
    for line in data[1:]:
        parts = line.split()
        r1, r2, r3 = int(parts[2]), int(parts[3]), int(parts[4])
        total = r1 + r2 + r3
        if total >= n and r1 >= m and r2 >= m and r3 >= m:
            valid.append((parts[0], parts[1], parts[2], parts[3], parts[4], str(total)))
    with open("exam.csv", "w", encoding="utf-8") as f:
        f.write("Фамилия;имя;результат 1;результат 2;результат 3;сумма\n")
        for rec in valid:
            f.write(";".join(rec) + "\n")