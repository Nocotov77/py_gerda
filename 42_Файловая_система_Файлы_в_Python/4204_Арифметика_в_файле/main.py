with open("in_file.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()
results = []
for line in lines:
    if line:
        parts = line.split()
        a = int(parts[0])
        op = parts[1]
        b = int(parts[2])
        if op == '+':
            res = a + b
        elif op == '-':
            res = a - b
        else:
            res = a * b
        results.append(f"{line} = {res}")
with open("out_file.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(results))