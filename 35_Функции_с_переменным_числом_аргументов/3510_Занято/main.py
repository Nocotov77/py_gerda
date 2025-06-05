def sequence_occupied(**kwargs):
    for row, seats in kwargs.items():
        for s in seats:
            places[int(row) - 1][s - 1] = 1
    best, best_row = 0, 0
    for i, row in enumerate(places):
        count, max_count = 0, 0
        for seat in row:
            if seat == 1:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 0
        if count > max_count:
            max_count = count
        if max_count > best:
            best = max_count
            best_row = i + 1
    return best, best_row