num = int(input())
num2 = 0
while num > 0:
    f = num % 10
    num = num // 10
    num2 *= 10
    num2 += f
print(num2)
