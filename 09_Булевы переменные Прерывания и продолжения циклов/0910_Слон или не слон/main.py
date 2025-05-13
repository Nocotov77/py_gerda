trunk = 0
tail = 0
legs = 0
ears = 0
eyes = 0
mouth = 0
elephant = 0

while True:
    n = int(input())
    s = input()
    match s:
        case "хобот":
            trunk += n
        case "хвост":
            tail += n
        case "нога":
            legs += n
        case "ухо":
            ears += n
        case "глаз":
            eyes += n
        case "рот":
            mouth += n
        case "ОБЕД":
            break
    if trunk >= 1 and tail >= 1 and legs >= 4 and ears >= 2 and eyes >= 2 and mouth >= 1:
        elephant = min(trunk, tail, legs / 4, ears / 2, eyes / 2, mouth)
        break

if elephant > 0:
    print("Есть слон!", str(int(elephant)), sep="\n")
else:
    print("Какие-то слоны нецелые. Пошли обедать.")