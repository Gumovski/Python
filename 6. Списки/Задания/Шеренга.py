s = list(map(int, input().split()))
p = int(input())
count = 0
for i in range(len(s)):
    if s[i] >= p:
        count += 1
print(count + 1)