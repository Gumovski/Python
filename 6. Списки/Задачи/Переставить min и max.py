s = list(map(int, input().split()))
a = []
for j in range(len(s)):
    a.append(s[j])
w = 0
q = 0
a.sort()
mini = a[0]
maxi = a[len(s) - 1]
for i in range(len(s)):
    if mini == s[i]:
        q = i
    if maxi == s[i]:
        w = i
s[w], s[q] = s[q], s[w]
print(s)