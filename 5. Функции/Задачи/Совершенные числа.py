def perfect(n):
    summ = 0
    for i in range(1, n):
        if n % i == 0:
            summ += i
    return summ == n

def perfect_num(count):
    a = 0
    n = 1
    while a < count:
        if perfect(n):
            print(n)
            a += 1
        n += 1
count = int(input())
perfect_num(count)
