dreams = []
while True:
    line = input().strip()
    if not line:
        break
    dreams.append(line)

if not dreams:
    print("")
else:
    a = int(input())
    b = int(input())

    start_night = min(a, b)
    end_night = max(a, b)

    start_index = max(0, start_night - 1)
    end_index = min(len(dreams) - 1, end_night - 1)

    selected_dreams = dreams[start_index: end_index + 1]

    max_length = -1
    longest_dream = ""
    for dream in selected_dreams:
        if len(dream) > max_length:
            max_length = len(dream)
            longest_dream = dream

    print(longest_dream)