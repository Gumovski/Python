n, m, k = list(map(int,input().split()))
matrix = [[0 for i in range(n)] for j in range(m)]
for i in range(k):
    x, y = list(map(int, input().split()))
    matrix[x][y] = '*'
    if matrix[x][y - 1] != '*':
        matrix[x][y - 1] += 1

    if matrix[x][y + 1] != '*':
        matrix[x][y + 1] += 1

    if matrix[x - 1][y] != '*':
        matrix[x - 1][y] += 1

    if matrix[x + 1][y] != '*':
        matrix[x + 1][y] += 1

    if matrix[x - 1][y - 1] != '*':
        matrix[x - 1][y - 1] += 1

    if matrix[x - 1][y + 1] != '*':
        matrix[x - 1][y + 1] += 1

    if matrix[x + 1][y - 1] != '*':
        matrix[x + 1][y - 1] += 1

    if matrix[x + 1][y + 1] != '*':
        matrix[x + 1][y + 1] += 1

