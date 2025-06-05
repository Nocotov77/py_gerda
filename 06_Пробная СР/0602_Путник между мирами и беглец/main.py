p = float(input())
g = float(input())
k = float(input())
d = int(input())
t = int(input())
T = t / 60
res = []
if p * T >= d:
    res.append("человек")
if g * T >= d:
    res.append("геддар")
if k * T >= d:
    res.append("кханнан")
print(" ".join(res) if res else "Не они")
