n, m, k = list(map(int,input().split()))
matrix = [[0 for i in range(m)] for j in range(n)]
for i in range(k):
    x, y = list(map(int, input().split()))
    matrix[x][y] = '*'

    if y > 0 and matrix[x][y - 1] != '*':
        matrix[x][y - 1] += 1
    #
    if matrix[x][y + 1] != '*':
        if y != m :
            matrix[x][y + 1] += 1
    #
    if matrix[x - 1][y] != '*':
        if x != 0:
            matrix[x - 1][y] += 1
    #
    if matrix[x + 1][y] != '*':
        if x != n :
            matrix[x + 1][y] += 1
    #
    if matrix[x - 1][y - 1] != '*':

        matrix[x - 1][y - 1] += 1
    #
    if matrix[x - 1][y + 1] != '*':
        matrix[x - 1][y + 1] += 1
    #
    if matrix[x + 1][y - 1] != '*':
        matrix[x + 1][y - 1] += 1
    #
    if matrix[x + 1][y + 1] != '*':
        matrix[x + 1][y + 1] += 1

for

def print_matrix(matrix):
    for row in matrix:
        for i in row:
            print(f'{i:<3d}', end='')
        print()

print_matrix((7, 10))