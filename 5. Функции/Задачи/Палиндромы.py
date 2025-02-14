def is_palindrome(num):
    num2 = 0
    old = num
    while num > 0:
        num2 = (num2 * 10 ) + (num % 10)
        num = num // 10
    return old == num2
a = int(input())
b = int(input())
count = 0
for i in range(a, b+1):
    if is_palindrome(i):
        count += 1
print(count)