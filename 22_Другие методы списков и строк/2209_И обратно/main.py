intervals = list(map(int, input().split()))
start, end = map(int, input().split())

s = min(start, end)
e = max(start, end)

total = sum(intervals[s:e])

print(total)