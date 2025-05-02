def multiply(n,m):
    return [[i*j for i in range(n)] for j in range(m)]

def chess_order(n, m):
    return [[1 if (i + j) % 2 == 0 else 0 for i in range(n)] for j in range(m)]
def cross(n):
    return [[1 if (i == j or i + j == n - 1) else 0 for j in range(n)] for i in range(n)]

def quadrants(n):
    return[]

###
def print_matrix(matrix):
    for row in matrix:
        for i in row:
            print(f'{i:<3d}', end='')
        print()
print_matrix(cross(8))
###

