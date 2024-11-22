n = int(input())
positive = 0
negative = 0
zero = 0
for i in range(n):
    a = int(input())
    if a > 0:
        negative += 1
    elif a < 0:
        positive += 1
    else:
        zero += 1
print(f'Положительный:{negative}')
print(f'Отрицательных:{positive}')
print(f'Нулей: {zero}')
