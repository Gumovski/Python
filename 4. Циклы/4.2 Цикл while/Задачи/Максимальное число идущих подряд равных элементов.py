a = int(input())
pre = 0
countmx = 0
count = 0
while a != 0:
    if a == pre:
        count += 1
    else:
        count = 0
    if count > countmx:
        countmx = count
    pre = a
    a = int(input())
print(countmx + 1)
