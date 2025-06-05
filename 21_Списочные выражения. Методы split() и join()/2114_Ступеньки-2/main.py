n = int(input())
groups = [
    ", ".join(map(str, range(i, min(i + 4, n + 1))))
    for i in range(1, n + 1, 4)
]
result = "; АХ! ".join(groups) + ("; АХ! " if n % 4 == 0 else "")
print(result)