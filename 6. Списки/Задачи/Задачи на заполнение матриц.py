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
    pass

###
def print_matrix(matrix):
    for row in matrix:
        for i in row:
            print(f'{i:<3d}', end='')
        print()
print_matrix(quadrants(8))
###

