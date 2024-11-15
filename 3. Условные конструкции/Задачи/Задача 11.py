a = int(input())
b = int(input())
c = int(input())
cos = (a**2 + b**2 - c**2) / 2 * a * b
if cos > 1:
    print('Не существует')
else:
    if cos == 0:
        print('Прямоугольный')
    elif cos > 0:
        print('Остроугольный')
    elif cos < 0:
        print('Тупоугольный')