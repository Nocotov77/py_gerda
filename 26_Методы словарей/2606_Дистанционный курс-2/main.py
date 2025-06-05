n = int(input())
students = {}
for _ in range(n):
    line = input()
    head, score = line.split(": ")
    score = int(score)
    name = head.split(" (")[0]
    mod = int(head.split(" (")[1].split(")")[0].split()[1])
    students.setdefault(name, {})[mod] = students.setdefault(name, {}).get(mod, 0) + score
for name, mods in students.items():
    if all(m in mods for m in range(1, 6)) and sum(mods.values()) >= 75:
        print(name)
