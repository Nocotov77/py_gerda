import sys

lines = sys.stdin.read().splitlines()
with open("plantis.csv", "w", encoding="utf-8") as f:
    f.write("nomen;definitio;pluma;Russian nomen;familia;Russian nomen familia\n")
    for line in lines:
        if line.strip():
            f.write(";".join(line.split("\t")) + "\n")