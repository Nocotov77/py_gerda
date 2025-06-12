import csv

with open("yndx_share_price.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    prices = [float(row[2]) for row in reader]
n = len(prices)
res = [0] * n
stack = []
for i in range(n - 1, -1, -1):
    while stack and prices[stack[-1]] <= prices[i]:
        stack.pop()
    res[i] = stack[-1] - i if stack else 0
    stack.append(i)
with open("predict.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(str(x) for x in res))