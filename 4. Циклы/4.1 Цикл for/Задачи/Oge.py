n = int(input())
summa = 0
while n != 0:
    if n % 10 == 4 and n % 6 == 0:
        summa += n
    n = int(input())
print(summa)