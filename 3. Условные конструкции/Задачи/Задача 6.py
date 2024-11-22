a = int(input())
b = int(input())
c = int(input())
# Теоремой Пифагора
# Найти Гипотенузу и катеты
if c**2 == a**2 + b**2 or a**2 == b**2 + c**2 or b**2 == a**2 + c**2:
    print('Прямоугольный')
else:
    if c**2 > a**2 + b**2 or a**2 > b**2 + c**2 or b**2 > a**2 + c**2:
        print('Тупоугольный')
    else:
        if c**2 < a**2 + b**2 or a**2 < b**2 + c**2 or b**2 < a**2 + c**2:
            print('Остроугольный')
        else:
            print('Остроугольный')

