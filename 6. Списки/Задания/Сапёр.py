def supior(n, m, k):
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
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
            if i == 0:
                print('.', end='')
            else:
                print(i, end='')
        print()

n, m, k = list(map(int, input().split()))
print_matrix(supior(n, m, k))
