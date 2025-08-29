n, m = list(map(int, input().split()))
matrix = []
mai = 0
maj = 0
for i in range(n):
    matrix.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix[mai][maj]:
            mai = i
            maj = j
print(mai, maj)