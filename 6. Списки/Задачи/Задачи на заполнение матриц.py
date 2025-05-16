def multiply(n, m):
    return [[i*j for i in range(n)] for j in range(m)]

def chess_order(n, m):
    return [[1 if (i + j) % 2 == 0 else 0 for i in range(n)] for j in range(m)]

def cross(n):
    return [[1 if (i == j or i + j == n - 1) else 0 for j in range(n)] for i in range(n)]

def quadrants(n):
    return [[0 if (i == j or i + j == n - 1) else 3 if (i > j and i + j > n - 1) else 4 if (i > j and i + j < n - 1) else 1 if (i < j and i + j < n - 1) else 2 for j in range(n) ] for i in range(n)]

def nested_rectangles(n, m):
    return [[min(i, j, m - 1 - i, n - 1 - j) for j in range(n)] for i in range(m)]

def spiral(n, m):
    matrix = [[0 for i in range(m)]for j in range(n)]
    x = 0
    up = 0
    down = n - 1
    left = 0
    right = m - 1
    while n*m >= x:
        for j in range(left,right + 1):
            matrix[up][j] = x
            x += 1
        up += 1
        if n*m == x:
            break
        for i in range(up,down + 1):
            matrix[i][right] = x
            x += 1
        right -= 1
        if n*m == x:
            break
        for j in range(right, left - 1, -1):
            matrix[down][j] = x
            x += 1
        down -= 1
        if n*m == x:
            break
        for i in range(down,up - 1, -1):
            matrix[i][left] = x
            x += 1
        left += 1
    return matrix
###
def print_matrix(matrix):
    for row in matrix:
        for i in row:
            print(f'{i:<3d}', end='')
        print()
print_matrix(spiral(7,10))
###

