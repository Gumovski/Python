s = input()
k, m = map(int,input().split())
result = ''
allowed = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

dec = 0
for i in s:
    if i in allowed:
        value = allowed.index(i)
        dec =  (dec * k) + value

while dec > 0:
    result = result + allowed[dec % m]
    dec = dec // m
if s[0] == '-':
    print(f'-{result[::-1]}')
else:
    print(result[::-1])