with open("messier.txt", "r", encoding="utf-8") as fin, open("messier.csv", "w", encoding="utf-8") as fout:
    for line in fin:
        fout.write(";".join(line.rstrip("\n").split("\t")) + "\n")