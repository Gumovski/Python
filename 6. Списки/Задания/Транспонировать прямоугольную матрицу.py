n, m = list(map(int, input().split()))
matrix = []
for s in range(n):
    matrix.append(list(map(int, input().split())))

tmp = []
for j in range(m):
    row = []
    for i in range(n):
        row.append(matrix[i][j])
    tmp.append(row)
for row in tmp:
    print(*row)
