s = input().strip()
unique_chars = set(s)
codes = [ord(c) for c in unique_chars]
min_code = min(codes) if codes else 0
max_code = max(codes) if codes else 0
print(f"{min_code}, {max_code}")
print("ХВАТИТ" if len(unique_chars) <= 32 else "НЕ ХВАТИТ")