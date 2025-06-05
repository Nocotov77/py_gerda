w = input().strip()
if len(w) > 13 or not ("беззар" <= w <= "хлябь") or "мир" in w or ("стан" in w and len(w) % 2 == 0):
    print("НЕ МОЖЕТ")
else:
    print("МОЖЕТ")