a = int(input())
for i in range(1, a):
    for j in range(1, a):
        print(f'{i * j:<3d}', end='')
    print()
