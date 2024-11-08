a = int(input())
b = int(input())
c = int(input())
s = a % 60
mi = (a - s) // 60
m = mi % 60
h = mi // 60

s1 = b % 60
mi1 = (b - s1) // 60
m1 = mi1 % 60
h1 = mi1 // 60

s2 = c % 60
mi2 = (c - s2) // 60
m2 = mi2 % 60
h2 = mi2 // 60

print(h,m,s)
print(h1,m1,s1)
print(h2,m2,s2)

