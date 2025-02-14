a = int(input())

if 10 < a % 100 < 15:
    print('грибов')
elif 2 <= a % 10 <= 4:
    print('гриба')
elif a % 10 == 1:
    print('гриб')
else:
    print('грибов')
