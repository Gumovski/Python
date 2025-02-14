def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


a = int(input())
n = 1
count = 0
while a > count:
    if is_prime(n):
        count += 1
        print(n)
    n += 1