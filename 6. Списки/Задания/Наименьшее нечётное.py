s = list(map(int, input().split()))
s.sort()
a = 0
for i in range(len(s)):
    if s[i] % 2 != 0:
        a = s[i]
        break
print(a)