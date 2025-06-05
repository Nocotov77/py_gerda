n = int(input())
m = int(input())
total = (n + m - 1) // m
r = 0
while r < total:
    row_str = ""
    row_start = r * m + 1
    if r == total - 1 and n % m != 0:
        count = n - r * m
        row_finish = n
    else:
        count = m
        row_finish = r * m + m
    c = 0
    while c < m:
        if r % 2 == 0:
            if c < count:
                row_str += str(row_start + c)
            else:
                row_str += ""
        else:
            if count == m:
                row_str += str(row_finish - c)
            else:
                if c < m - count:
                    row_str += ""
                else:
                    row_str += str(row_finish - (c - (m - count)))
        if c < m - 1:
            row_str += "\t"
        c += 1
    print(row_str)
    r += 1