n = int(input())
cntmin = 0
cntplus = 0
cntzero = 0
for i in range(n):
    a = int(input())
    if a > 0:
        cntplus += 1
    else:
        if a < 0:
            cntmin += 1
        else:
            if a == 0:
                cntzero += 1
print(f'Положительный:{cntplus}')
print(f'Отрицательных:{cntmin}')
print(f'Нулей: {cntzero}')