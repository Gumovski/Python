a = int(input())

if a % 100 == 11 or a % 100 == 12 or a % 100 == 13 or a % 100 == 14:
    print('грибов')
else:
    if a % 10 == 2 or a % 10 == 3 or a % 10 == 4:
        print('гриба')
    elif a % 10 == 1:
        print('гриб')
    elif a % 10 == 0:
        print('грибов')
    elif a % 10 == 5 or a % 10 == 6 or a % 10 == 7 or a % 10 == 8 or a % 10 == 9:
        print('грибов')
