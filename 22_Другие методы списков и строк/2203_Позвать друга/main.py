messages = []
while True:
    line = input()
    if line == "":
        break
    messages.append(line)
username = input().strip()

selected = []
prefix = f"@{username} "
for msg in messages:
    if msg.startswith(prefix):
        content = msg[len(prefix):].strip()
        if content:
            formatted = content[0].upper() + content[1:].lower()
            selected.append(formatted)

selected.sort()
for item in selected:
    print(item)