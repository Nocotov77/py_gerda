def write_file(file, memory, capacity=1):
    free = []
    for i in range(len(memory)):
        for j in range(len(memory[i])):
            if memory[i][j] == 0:
                free.append((i, j))
    req = (len(file) + capacity - 1) // capacity
    if len(free) < req:
        return
    for idx in range(req):
        chunk = file[idx * capacity:(idx + 1) * capacity]
        nxt = free[idx + 1] if idx < req - 1 else (None, None)
        i, j = free[idx]
        memory[i][j] = (chunk, nxt[0], nxt[1])


def read_file(memory, start):
    s = ""
    cur = start
    while True:
        i, j = cur
        cell = memory[i][j]
        if not isinstance(cell, tuple):
            break
        chunk, ni, nj = cell
        s += chunk
        if ni is None and nj is None:
            break
        cur = (ni, nj)
    return s


memory = [['*', 0, 0, '*', '*'],
          ['*', '*', '*', 0, 0],
          [0, '*', '*', '*', '*']]
file = 'Abracadabra'
write_file(file, memory, capacity=3)
for i in range(len(memory)):
    print(*memory[i], sep='\t')