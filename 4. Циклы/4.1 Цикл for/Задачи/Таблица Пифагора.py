a = int(input())
for i in range(a):
    for j in range(a):
        if i * j == 0:
            print(f"")
        elif i * j < 10:
            print(i * j, end = '  ')
        else:
            print(i * j, end=' ')
