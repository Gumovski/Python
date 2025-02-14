a = int(input())
max = 0
count = 0
while a != 0:
    if a > max:
        max = a
        count = 0
    if a == max:
        count += 1
    a = int(input())
print(count)
