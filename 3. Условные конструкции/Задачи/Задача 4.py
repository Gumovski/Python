a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

a = a2- a1
b = b2 - b1
if ((a == b or a == -b) or (a1 == a2 or b1 == b2)) and (a2 - a1 != 0 or b2 - b1 != 0):
    print('Yes')
else:
    print('No')