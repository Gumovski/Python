n, m = list(map(int, input().split()))
matrix = []
for s in range(n):
    matrix.append(list(map(int, input().split())))

tmp = []
for j in range(m):
    row = []
    for i in range(n):
        row.append(matrix[i][j])
    for k in range(len(row) // 2):
        row[k], row[len(row) - 1 - k] = row[len(row) - 1 - k], row[k]
    tmp.append(row)
for row in tmp:
    print(*row)