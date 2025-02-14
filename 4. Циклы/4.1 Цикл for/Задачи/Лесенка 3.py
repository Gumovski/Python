n = int(input('Введите количество повторений:'))
for i in range(n):
    for j in range(n, i, -1):
        print(j, end ="")
    print()
