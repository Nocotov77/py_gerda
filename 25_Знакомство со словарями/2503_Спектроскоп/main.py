d = {}
while True:
    s = input()
    if s == "":
        break
    a = s.split()
    d[a[0]] = set(a[1:])
obs = set()
while True:
    s = input()
    if s == "":
        break
    obs.add(s)
for k, v in d.items():
    if v.issubset(obs):
        print(k)
