n = int(input())
s = list(map(int, input().split()))
k, m, d = list(map(int, input().split()))
s = s[:k - 1] + sorted(s[k - 1:m:], reverse = d == -1) + s[m:]
print(s)
