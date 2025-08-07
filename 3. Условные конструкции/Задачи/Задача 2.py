a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if ( -1 <=  a2 - a1 <= 1 ) and (-1 <= b2- b1 <= 1) and (a2 - a1 != 0 or b2 - b1 != 0):
    print('Yes')
else:
    print('No')