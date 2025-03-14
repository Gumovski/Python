s = list(map(int, input().split()))
mini = s[0]
maxi = s[0]
for i in range(len(s)):
    if s[i] > maxi:
        maxi = s[i]
    if s[i] < mini:
        mini = s[i]

print(s)
