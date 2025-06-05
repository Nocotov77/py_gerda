def supercargo_2(load, capacity):
    def digits(x, d):
        return len(str(abs(x))) == d
    decks = [
        ["lower", capacity[2], lambda x: digits(x, 3)],
        ["middle", capacity[1], lambda x: digits(x, 2)],
        ["upper", capacity[0], lambda x: digits(x, 1)]
    ]
    deck_index = 0
    while deck_index < len(decks) and decks[deck_index][1] == 0:
        deck_index += 1
    unassigned = []
    for cargo in load:
        if deck_index < len(decks):
            if decks[deck_index][2](cargo) and decks[deck_index][1] > 0:
                decks[deck_index][1] -= 1
                if decks[deck_index][1] == 0:
                    deck_index += 1
                    while deck_index < len(decks) and decks[deck_index][1] == 0:
                        deck_index += 1
            else:
                unassigned.append(cargo)
        else:
            unassigned.append(cargo)
    fully_loaded = (decks[0][1] == 0 and decks[1][1] == 0 and decks[2][1] == 0)
    return (tuple(unassigned), fully_loaded)