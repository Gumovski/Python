a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

a = a2- a1
b = b2 - b1
if  (a * b == 2 or a * b == -2) and (a != 0 and b != 0):
    print('Yes')
else:
    print('No')