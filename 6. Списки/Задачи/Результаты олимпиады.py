n = int(input())
s = []
for i in range(n):
    name, score = input().split()
    s.append([name, int(score)])
s.sort(key=lambda x: x[1], reverse=True)

for j in s:
    print(j[0])
