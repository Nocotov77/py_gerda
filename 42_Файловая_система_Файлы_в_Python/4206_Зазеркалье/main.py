fn = input().strip()
with open(fn, "rb") as f:
    lines = f.read().splitlines()
with open("output.dat", "wb") as out:
    for line in lines:
        s = line.decode("utf-8")
        rs = s[::-1]
        out.write(rs.encode("utf-8") + b'\n')