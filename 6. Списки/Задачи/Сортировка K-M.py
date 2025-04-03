n = int(input())
s = list(map(int, input().split()))
k, m, d = list(map(int, input().split()))

if d == -1:
    s = s[:k - 1] + sorted(s[k - 1:m:], reverse=True) + s[m:]
else:
    s = s[:k - 1] + sorted(s[k - 1:m:]) + s[m:]
print(s)
