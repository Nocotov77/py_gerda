def price(a, b, c):
    with open("borsch.txt", "r", encoding="utf-8") as f:
        prices = [float(line.strip()) for line in f if line.strip()]
    print(a * prices[0] + b * prices[1] + c * prices[2])