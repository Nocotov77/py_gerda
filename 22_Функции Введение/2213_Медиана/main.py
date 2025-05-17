def median(data):
    data.sort()
    n = len(data)
    if n % 2 == 1:
        print(data[n // 2])
    else:
        print((data[n // 2 - 1] + data[n // 2]) / 2)