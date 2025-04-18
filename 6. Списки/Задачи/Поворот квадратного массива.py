n = int(input())
matrix = []
for s in range(n):
    matrix.append(list(map(int, input().split())))
for i in range(n):
    for j in range(i+1, n):
        matrix[i][j], matrix[j][i] =  matrix[j][i], matrix [i][j]
for i in range(n):
    for j in range(n // 2):
        k = n - 1 - j
        matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
print(matrix)