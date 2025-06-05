def get_medicine(matrix, k=0):
    n = len(matrix)
    if k == 0:
        return
    elif k == 1:
        for i in range(1, n, 2):
            matrix[i], matrix[i - 1] = matrix[i - 1], matrix[i]
    elif k == 2:
        for i in range(n):
            for j in range(1, n, 2):
                matrix[i][j], matrix[i][j - 1] = matrix[i][j - 1], matrix[i][j]
    elif k == 3:
        for i in range(1, n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    elif k == 4:
        new = [[matrix[n - 1 - j][n - 1 - i] for j in range(n)] for i in range(n)]
        for i in range(n):
            matrix[i][:] = new[i][:]