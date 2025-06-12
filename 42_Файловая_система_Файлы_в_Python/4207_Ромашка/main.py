start = input().strip()
n = int(input().strip())
result = start if n % 2 == 1 else ("не любит" if start == "любит" else "любит")
with open("fortune.txt", "w", encoding="utf-8") as f:
    f.write(result)