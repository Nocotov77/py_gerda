def horse2(pos):
    col = ord(pos[0]) - ord('a')
    row = int(pos[1]) - 1
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    for dx, dy in moves:
        nc, nr = col + dx, row + dy
        if 0 <= nc < 8 and 0 <= nr < 8:
            print(chr(nc + ord('a')) + str(nr + 1))