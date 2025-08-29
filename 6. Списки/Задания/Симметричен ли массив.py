#Симметричен ли массив
n = int(input())
matrix = []
for s in range(n):
    matrix.append(list(map(int, input().split())))
def is_symmetric(matrix):
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
print('Yes' if is_symmetric(matrix) else 'No')