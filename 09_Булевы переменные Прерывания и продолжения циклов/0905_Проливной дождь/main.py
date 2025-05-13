size_bucket = int(input())
counter = 0
grad = False

while True:
    n = int(input())
    counter += 1
    if n == 0:
        break
    if n > 20:
        grad = True
    size_bucket -= n
    if size_bucket <= 0:
        print(f"Время заполнения {counter} секунд.")
        break

if size_bucket > 0:
    print("Ведро не полное.")

if grad:
    print("Град был!")
else:
    print("Града не было.")