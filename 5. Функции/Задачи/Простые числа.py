a = int(input())
n = 1
count = 0
while a > count:
    n += 1
    p = 0
    for i in range(1, n+1):
        if n % i == 0:
            p += 1
    if p == 2:
        count += 1
        print(n)