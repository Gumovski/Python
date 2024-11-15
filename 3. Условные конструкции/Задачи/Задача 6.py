a = int(input())
b = int(input())
c = int(input())
# Теоремой Пифагора
# Найти Гипотенузу и катеты
cos = (a**2 + b**2 - c**2) / 2 * a * b
if cos > 1:
    print('Не существует')
elif cos == 0:
    print('Прямоугольный')
elif cos > 0:
    print('Остроугольный')
elif cos < 0:
    print('Тупоугольный')