nums = list(map(int, input().split()))
res = []
for num in nums:
    b = bin(num)[2:]
    res.append({"digits": len(b), "units": b.count("1"), "zeros": b.count("0")})
print(res)
