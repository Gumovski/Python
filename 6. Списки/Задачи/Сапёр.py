def supior(n,m,k):
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        matrix[x][y] = '*'

        if y > 0 and matrix[x][y - 1] != '*':
            matrix[x][y - 1] += 1

        if y < m - 1 and matrix[x][y + 1] != '*':
            matrix[x][y + 1] += 1

        if x > 0 and matrix[x - 1][y] != '*':
            matrix[x - 1][y] += 1

        if x < n - 1 and matrix[x + 1][y] != '*':
            matrix[x + 1][y] += 1

        if x > 0 and y > 0 and matrix[x - 1][y - 1] != '*':
            matrix[x - 1][y - 1] += 1

        if x > 0 and y < m - 1 and matrix[x - 1][y + 1] != '*':
            matrix[x - 1][y + 1] += 1

        if x < n - 1 and y > 0 and matrix[x + 1][y - 1] != '*':
            matrix[x + 1][y - 1] += 1

        if x < n - 1 and y < m - 1 and matrix[x + 1][y + 1] != '*':
            matrix[x + 1][y + 1] += 1

    return matrix

def print_matrix(matrix):
    for row in matrix:
        for i in row:
            print(f'{i:<3}', end='')
        print()
print_matrix(supior(10, 9, 23))
#1 8
#2 3
#3 2
#3 3
#4 3
#5 7
#6 7
#7 1
#7 2
#7 3
#7 4
#7 5
#7 6
#7 7
#7 8
#8 1
#8 3
#8 5
#8 7
#9 3
#9 5
#9 6
#9 7